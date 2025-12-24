import pandas as pd
sales_df = pd.read_csv("C:\\Users\\SHIVAJI\\Downloads\\fmcg_sales_3years_1M_rows.csv",
                       low_memory=False)
store = sales_df.drop_duplicates(subset=['store_id'])
store_df = pd.DataFrame({
    "store_id": store['store_id'],
    "country": store['country'],
    "city": store['city'],
    "channel": store['channel'],
    "latitude": store['latitude'],
    "longitude": store['longitude']
})
store_df.to_csv("store.csv", index=False)
print(store_df.head())

supplier_df = sales_df.drop_duplicates(subset=['supplier_id'])
supplier_data = pd.DataFrame({
    "supplier_id": supplier_df['supplier_id']
})
supplier_data.to_csv("supplier.csv",index=False)
print(supplier_data.head())

products = sales_df.drop_duplicates(subset=['sku_id'])
products_df= pd.DataFrame({
    "sku_id": products['sku_id'],
    "sku_name": products['sku_name'],
    "category": products['category'],
    "subcategory": products['subcategory'],
    "brand": products['brand']
})
products_df.to_csv("products.csv",index=False)
print(products_df.head())


date_dt = sales_df.drop_duplicates(subset=['date'])
date_df= pd.DataFrame({
    "date_id": date_dt['date'],
    "year": date_dt['year'],
    "month": date_dt['month'],
    "day": date_dt['day'],
    "weekofyear": date_dt['weekofyear'],
    "weekday": date_dt['weekday'],
    "is_weekend": date_dt['is_weekend'],
    "is_holiday": date_dt['is_holiday']
})
date_df.to_csv("date_info.csv",index=False)


weather_df = sales_df.drop_duplicates(subset=['store_id','date'])

weather = pd.DataFrame({
    "store_id": weather_df['store_id'],
    "date_id": weather_df['date'],
    "temperature": weather_df['temperature'],
    "rain_mm": weather_df['rain_mm']
})
weather.to_csv("weather.csv",index=False)
print(weather.head())

sales=pd.DataFrame({
    "date_id":sales_df["date"],
    "store_id":sales_df["store_id"],
    "sku_id":sales_df["sku_id"],
    "supplier_id":sales_df["supplier_id"],
    "lead_time_days": sales_df['lead_time_days'],
    "purchase_cost": sales_df['purchase_cost'],
    "list_price": sales_df['list_price'],
    "units_sold":sales_df["units_sold"],
    "discount_pct":sales_df["discount_pct"],
    "promo_flag":sales_df["promo_flag"],
    "gross_sales":sales_df["gross_sales"],
    "net_sales":sales_df["net_sales"],
    "stock_on_hand":sales_df["stock_on_hand"],
    "stock_out_flag":sales_df["stock_out_flag"],
    "margin_pct":sales_df["margin_pct"]
})
sales.to_csv("sales.csv",index=False)
print(sales.head())