# Product SDD quality checklist

- [ ] Сценарии читаются без открытия прототипа.
- [ ] Каждое GWT проверяет observable requirement, а не CSS/DOM/API/DTO detail.
- [ ] States и transitions описаны предметным языком.
- [ ] Error matrix содержит condition, system reaction, user-visible result и recovery.
- [ ] Business rules используют предметные термины, а не prototype/transport parameter names.
- [ ] Permission включён только там, где он влияет на user-visible behavior.
- [ ] Hardcoded prototype/spec implementation values не объявлены product constraints без продуктового источника.
- [ ] Analytical specs загружены выборочно через index, а не целиком.
- [ ] Технические факты из analytical specs преобразованы в observable behavior.
- [ ] В документе нет endpoint/DTO/storage/component/store/backend implementation design.
- [ ] Intent не переписан и не расширен implementation details.
- [ ] Deviations взяты из approved UX Sync.
- [ ] Для ключевых требований есть traceability.
- [ ] Unknowns не выданы за факты; needs-review/unknown analytical sources отмечены корректно.
- [ ] Engineering dependencies отделены от product/domain open questions.
