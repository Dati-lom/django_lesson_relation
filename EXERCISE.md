# Django ModelAdmin - პრაქტიკული დავალება
- შექმენით superuser: `python manage.py createsuperuser`
### დავალება 1.1: Category ModelAdmin

დააკონფიგურირეთ `CategoryAdmin` შემდეგი მოთხოვნებით:

- **list_display**: გამოაჩინეთ `id`, `name`, და `description`
- **search_fields**: ძიება შესაძლებელი უნდა იყოს `name`-ის მიხედვით
- **ordering**: კატეგორიები დალაგებული უნდა იყოს `name`-ის ანბანის მიხედვით
- **fields**: რედაქტირებისას გამოაჩინეთ მხოლოდ `name` და `description`

### დავალება 1.2: Item ModelAdmin

დააკონფიგურირეთ `ItemAdmin` შემდეგი მოთხოვნებით:

- **list_display**: გამოაჩინეთ `id`, `name`, `price`, და `category`
- **search_fields**: ძიება შესაძლებელი უნდა იყოს `name`-ის და `category__name`-ის მიხედვით
- **ordering**: Item-ები დალაგებული უნდა იყოს `price`-ის ზრდადობით
- **autocomplete_fields**: გამოიყენეთ autocomplete `category` ველისთვის

### დავალება 1.3: Inline ურთიერთობები

დაამატეთ `TabularInline` `CategoryAdmin`-ში დაკავშირებული Item-ების გამოსაჩენად:

- გამოაჩინეთ `name` და `price` ველები თითოეული Item-ისთვის
- დააყენეთ `extra = 2` რათა გამოჩნდეს 2 ცარიელი ფორმა ახალი Item-ების დასამატებლად
- შესაძლებელი გახადეთ Item-ების რედაქტირება პირდაპირ Category-ს გვერდიდან

## ნაწილი 2: გაფართოებული ფუნქციები 

### დავალება 2.3: Custom List Display მეთოდი

დაამატეთ custom მეთოდი `CategoryAdmin`-ში სახელად `get_first_five_items`:

- ეს მეთოდი უნდა აჩვენებდეს თითოეული კატეგორიის პირველ 5 Item-ს
- გამოაჩინეთ Item-ების სახელები მძიმით გამოყოფილი
- დაამატეთ ეს მეთოდი `list_display`-ში

**მოსალოდნელი შედეგი**: "Motherboard, CPU, RAM, SSD, GPU"

**მინიშნება**:

```python
def get_first_five_items(self, obj):
    items = obj.items.all()[:5]
    return ", ".join([item.name for item in items])

get_first_five_items.short_description = "First 5 Items"
```



### დავალება 2.5: დაკავშირებული ობიექტების ძიება

გახადეთ შესაძლებელი კატეგორიების ძიება Item-ების სახელების მიხედვით:

- დაამატეთ `items__name` `search_fields`-ში `CategoryAdmin`-ში
- გატესტეთ - მოძებნეთ Item-ის სახელი და დარწმუნდით რომ მისი Category გამოჩნდება
- გაიგეთ რომ ეს ქმნის INNER JOIN-ს Category და Item მოდელებს შორის

### დავალება 2.6: List Filters

დაამატეთ ფასის ფილტრი `ItemAdmin`-ში:

- გამოიყენეთ `list_filter = ('price',)` ძირითადი ფასის ფილტრისთვის
- გატესტეთ ადმინში

