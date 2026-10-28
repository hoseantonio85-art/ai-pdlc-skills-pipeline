# NORM Product Likeness

Use this reference to make an HTML prototype feel like the existing NORM product. These are prototype approximations distilled from the reference frontend, not production UI Kit API claims.

## Recognizable shell

- Place the product navigation on a light `#f0f2f5` menu background outside the white work surface. Keep product pages white.
- Let the work surface occupy the available height and start with a `24px 0 0 24px` radius on desktop.
- Keep content centered at `1240px`; use about `875px` on compact laptops. Do not stretch meaningful content across an ultrawide viewport just because space exists.
- Use generous page insets around the work surface, then compact spacing inside registries. NORM combines a calm shell with dense working content.
- Keep the page title visually strong but not promotional. Put count, short context and optional action near it; avoid a large explanatory hero.

## Surface grammar

- Use white as the main work surface and soft neutral fills for grouping. Avoid nesting every field in a separate white card.
- Entity cards normally use `24px` padding, `16px` radius and a quiet one-pixel inset border.
- On hover replace the inset line with a restrained shadow close to `0 0 1px rgba(36,41,46,.32), 0 4px 8px rgba(36,41,46,.12)`.
- Use `24px` or `32px` radii for larger attention, summary or assistant surfaces. Reserve these surfaces for meaningful grouping.
- Dividers are thin and neutral. Metadata is visually weaker than the conclusion or object name.

## Registry rhythm

- Align repeated attributes vertically, but keep every row a meaningful object card rather than a raw data grid.
- A standard card may be taller and more explanatory; a long operational registry may use a compact row-card. Choose by task, not by a universal density target.
- Keep identity in the main left content zone. Event/Measure references may place a compact status/date row above the title; this is not a mandatory leading status column. Use the selected service composition contract.
- Do not add a colored rail to every status when a chip already carries the state. Use a rail only for a selected object or an exceptional attention state.
- Use the whole entity card for opening the object; do not add a separate Open/View button. Filled buttons belong to exceptional row actions such as retry, approval or destructive recovery.

## Quick filters and attention zones

- Arrange quick filters in a compact wrapping row with `8px` horizontal and about `4px` vertical gaps.
- Use soft surfaces, counts and restrained active states. Filters support scanning; they should not dominate the page.
- For an overview, attention zones may be larger `24px`-radius cards with a count marker and a soft semantic background. Use them only when each zone leads to a filtered registry or drill-down.
- A subtle multicolour tint is valid for a special new/AI attention zone. Do not use it as general page decoration.

## Floating action dock

- The product dock is a real signature pattern: about `600px` wide on desktop, `24px` padding, `16px` gap, `32px` radius and a soft elevated shadow.
- Place it `16px` above the lower edge of the work surface and reserve at least `116px` of content space below the registry.
- Put one persistent contextual action and, when valid, one assistant/chat entry in the dock. Text buttons fill the available inner width equally; the assistant icon remains fixed-size.
- Do not repeat the same primary action in the page header, every row and the dock. If the dock owns the persistent action, the header normally does not.
- If the scenario has no persistent action, omit the dock even though it is recognizable.

## Object Modal likeness

- Use an overlay close to `rgba(36,40,43,.56)` with `24px` outer padding.
- A large Object Modal may grow to `1320px`, use `24px` radius and preserve stable controls near the upper-right corner.
- Keep header/context stable and scroll the content body. In Object View use one right action/meta rail for compact object context, history/service navigation and all object-level workflow/lifecycle actions; do not duplicate them in a bottom Footer.
- Previous/next controls belong outside or at the edge of the object surface and only when sequential review works in the prototype.
- Avoid a dashboard grid of equal metadata cards inside every modal. Prefer a compact meta line or two-column description block unless comparison is important.

## Assistant and magic accents

- Ordinary actions use the NORM green/neutral palette. AI is a separate semantic layer, not the brand colour of the whole interface.
- A magic/assistant entry may use a restrained cyan–indigo–violet gradient border or soft tint. Keep the control compact and label its intent.
- Use the gradient only on the assistant entry, AI banner or AI-generated block. Never spread it to normal buttons, tabs, statuses or backgrounds.
- Attach assistant output to a concrete task: explain a signal, summarize evidence or prepare an action for human confirmation.

## Product-likeness check

Before handoff, compare the result with this signature:

1. light neutral menu plus rounded white work surface;
2. strong title, dense business content and quiet metadata;
3. one hierarchy of actions, without duplicated primary CTA;
4. cards with inset borders and restrained hover elevation;
5. accurate large modal and optional dock geometry;
6. AI accent isolated from ordinary product controls.

Do not force every item into one screen. Select only the patterns justified by the UX Solution.


For the compact runtime profile see `norm-visual-dna.md`; for exact task-time composition use the pattern/organism registries rather than expanding this file into a universal screen recipe.
