import pandas as pd
import plotly.express as px

df=pd.read_csv("project.csv")

z=px.scatter(df,x="date",y="cases",color="country",size="cases",size_max=60)
z.show()
