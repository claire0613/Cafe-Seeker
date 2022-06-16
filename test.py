from data.api_helper import city_cafe_filter


result = city_cafe_filter(page=0, city='taipei', keyword='', price=0, wifi=0, vacancy=0, drinks=0, quiet=0, comfort=0,
                                  limited_time='', meal_selling='', rating=0)
print(result)