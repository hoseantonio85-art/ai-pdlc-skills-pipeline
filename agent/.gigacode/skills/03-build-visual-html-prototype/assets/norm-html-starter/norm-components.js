/* Small prototype primitives; no production UI Kit API imitation. */
window.Norm = (() => {
 const esc=v=>String(v??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
 const paths={search:'<circle cx="9" cy="9" r="6"/><path d="m14 14 4 4"/>',filter:'<path d="M3 5h14M6 10h8M9 15h2"/>',calendar:'<rect x="3" y="4" width="14" height="14" rx="2"/><path d="M3 8h14M7 2v4M13 2v4M7 12h2M11 12h2"/>',people:'<circle cx="8" cy="6" r="2.5"/><path d="M3 16c0-5 10-5 10 0M14 4a2 2 0 0 1 0 4M15 11c3 0 4 2 4 4"/>',arrow:'<path d="M3 10h14m-5-5 5 5-5 5"/>'};
 const icon=(name)=>`<svg class="norm-icon" viewBox="0 0 20 20" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round">${paths[name]||paths.people}</svg>`;
 const brand=(variant='brand')=>'<img class="brand-mark" src="assets/'+(variant==='ai'?'gradient-logo.svg':'icon_logo.svg')+'" alt="" width="40" height="40">';
 const card=(d)=>`<button class="entity-card" data-id="${esc(d.id)}"><span class="entity-main"><span class="entity-top"><span class="status status-${esc(d.color)}">${esc(d.statusLabel)}</span><span class="date-tag">${icon('calendar')}${esc(d.dateLabel)}</span><span class="quiet">${esc(d.elapsed||'')}</span></span><strong class="entity-title">${esc(d.title)}</strong><span class="entity-metrics">${d.metrics.map(m=>`<span class="metric"><small>${esc(m[0])}</small><strong>${esc(m[1])}</strong></span>`).join('')}</span></span><span class="entity-meta"><span class="meta-heading"><span>${esc(d.id)}</span><span>Автор: ${esc(d.owner)}</span></span><span class="entity-description">${esc(d.description)}</span><span class="entity-owner">${icon('people')}${esc(d.org)}</span></span></button>`;
 const query=(items,state)=>items.filter(d=>(state.scope!=='mine'||d.mine)&&(!state.quick.length||state.quick.includes(d.status))&&(!state.applied.status||d.status===state.applied.status)&&(!state.applied.from||d.date>=state.applied.from)&&(!state.applied.to||d.date<=state.applied.to)&&`${d.title} ${d.id} ${d.description} ${d.owner}`.toLocaleLowerCase('ru').includes(state.search.toLocaleLowerCase('ru')));
 const stack=[];let root,oldOverflow,background=[],sequence=0;
 const focusables=e=>[...e.querySelectorAll('button,a[href],input,select,textarea,[tabindex]')].filter(x=>!x.disabled&&x.tabIndex>=0&&!x.closest('[inert]')&&x.getClientRects().length);
 const suspend=elements=>elements.map(el=>{const inert=el.inert;el.inert=true;return {el,inert};});
 const restore=entries=>entries.forEach(({el,inert})=>el.inert=inert);
 const focusFirst=el=>(focusables(el)[0]||el).focus();
 function updateUnderlay(){
  root.classList.toggle('surface-root-drawer-only',stack.every(x=>x.type==='drawer'));
  root.querySelector('.surface-underlay')?.remove();
  if(stack.filter(x=>x.type==='object').length>1){const u=document.createElement('div');u.className='surface-underlay';u.setAttribute('aria-hidden','true');root.prepend(u);}
 }
 // All prototype surfaces share one lifecycle. Options are local, not a UI Kit API.
 const open=(html,trigger=document.activeElement,{type='object',scope,closeOnEscape}={})=>{
  if(!root){
   root=document.createElement('div');root.className='surface-root';document.body.append(root);
   oldOverflow=document.body.style.overflow;document.body.style.overflow='hidden';
   background=suspend([...document.body.children].filter(x=>x!==root&&!['SCRIPT','STYLE'].includes(x.tagName)));
  }
  const previous=stack.at(-1),contained=type==='drawer'&&scope!=='viewport'&&previous;
  // A contained drawer is a child of the parent shell; only its previous content is inert.
  const suspended=previous?suspend(contained?[...previous.el.children]:[previous.layer]):[];
  if(previous)previous.el.setAttribute('aria-modal','false');
  const el=document.createElement('section');el.className=type==='drawer'?'filter-drawer':type==='form'?'object-modal standard-modal':'object-modal';
  el.setAttribute('role','dialog');el.setAttribute('aria-modal','true');el.tabIndex=-1;el.innerHTML=html;
  const heading=el.querySelector('h2');
  if(heading){heading.id=heading.id||`norm-surface-title-${++sequence}`;el.setAttribute('aria-labelledby',heading.id);}else el.setAttribute('aria-label','Окно');
  let layer=el;
  if(type==='drawer'){
   layer=document.createElement('div');layer.className='drawer-scrim'+(contained?' drawer-contained':'');layer.append(el);
   (contained?previous.el:root).append(layer);
  }else root.append(el);
  const triggerId=trigger?.closest?.('[data-id]')?.dataset.id;
  stack.push({el,layer,trigger,triggerId,type,suspended,closeOnEscape:closeOnEscape??type!=='drawer'});updateUnderlay();
  el.querySelectorAll('[data-close-surface]').forEach(b=>b.addEventListener('click',()=>close()));focusFirst(el);return el;
 };
 const drawer=(html,trigger=document.activeElement,options={})=>open(html,trigger,{...options,type:'drawer'});
 const close=()=>{
  const x=stack.pop();if(!x)return;x.layer.remove();restore(x.suspended);
  if(!stack.length){root.remove();root=null;restore(background);background=[];document.body.style.overflow=oldOverflow;}
  else{stack.at(-1).el.setAttribute('aria-modal','true');updateUnderlay();}
  const replacement=x.triggerId?document.querySelector(`[data-id="${CSS.escape(x.triggerId)}"]`):null;
  const target=x.trigger?.isConnected&&!x.trigger.closest('[inert]')?x.trigger:replacement;
  if(target?.getClientRects().length)target.focus();
  else if(stack.length)focusFirst(stack.at(-1).el);
  else document.querySelector('[data-main-action]')?.focus();
 };
 document.addEventListener('keydown',e=>{
  if(!stack.length||e.defaultPrevented)return;
  if(e.key==='Escape'){if(stack.at(-1).closeOnEscape){e.preventDefault();close();}return;}
  if(e.key==='Tab'){
   const el=stack.at(-1).el,f=focusables(el),active=document.activeElement;
   if(!f.length){e.preventDefault();el.focus();}
   else if(e.shiftKey&&(active===f[0]||!f.includes(active))){e.preventDefault();f.at(-1).focus();}
   else if(!e.shiftKey&&(active===f.at(-1)||!f.includes(active))){e.preventDefault();f[0].focus();}
  }
 });
 document.addEventListener('focusin',e=>{const top=stack.at(-1);if(top&&!top.el.contains(e.target))focusFirst(top.el);});
 return {esc,icon,brand,card,query,open,drawer,close,get stack(){return stack.map(({el,type})=>({el,type}));}};
})();
