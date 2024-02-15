import random
import pandas as pd


lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})


from sklearn.preprocessing import OneHotEncoder

#создание экземпляра one-hot-encoder
encoder = OneHotEncoder(handle_unknown='ignore')

#выполняем горячее кодирование столбца whoAmI
encoder_df = pd.DataFrame(encoder.fit_transform(data[['whoAmI']]).toarray())

#Объединить столбцы с горячим кодированием обратно с исходным DataFrame
final_df = data.join(encoder_df)

#выводим результат
print(final_df)
