# Агент для получения ответа 
Это агент, который генерирует ответ, брать ли с собой зонт в зависимости от полученных агентом для доступа к API данных о погоде в городе нахождения пользователя.

**Класс действий:**

`action_get_answer`

**Параметры:**
1. `input_structure` - структура данных с информацией о городе-местоположении пользователя и погоде в нем;

**Ход работы агента:**
* Агент подключается к выбранному API-сервису и получает данные о погоде в градусах и информацию о дожде/солнце, идентифицируя автора
действия как пользователя, а город, в котором находится пользователь, - как местоположение пользователя;
* Затем генерируется необходимая конструкция для вызова агента интерпретации неатомарных действий. Пример этой конструкции показан ниже.
![МОИС](https://github.com/demidovetsdasha/sem4/blob/main/%D0%9C%D0%9E%D0%98%D0%A1/%D0%BB%D1%804/interpretation.png)

* Агент вызывается после завершения работы агента для доступа к API, который заполнил данными `input_structure`. Затем данный агент выполняет поиск
набора правил о том, при каких условиях пользователю следует взять с собой зонт, и использует их для создания связи между пользователем и объектом из
множества рекомендаций, который включает в себя to_take_umbrella_recommendation и not_to_take_umbrella_recommendation.

### Пример

Пример входной структуры:

![МОИС](https://github.com/demidovetsdasha/sem4/blob/main/%D0%9C%D0%9E%D0%98%D0%A1/%D0%BB%D1%804/input.png)

Пример логического правила:

![МОИС](https://github.com/demidovetsdasha/sem4/blob/main/%D0%9C%D0%9E%D0%98%D0%A1/%D0%BB%D1%804/output.png)

### Результат

Возможные результаты:

* `SC_RESULT_OK` - агент выдает рекомендацию, нужно ли брать зонт;
* `SC_RESULT_ERROR`- требуемые для получения рекомендации сущности не были найдены.
