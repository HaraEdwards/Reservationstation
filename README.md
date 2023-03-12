## Welcome
Hello and welcome to the Dataset for the reservation system used at a university for faculty students and staff. Here's a basic rundown of what I did to create this dataset and some of what it entails.

### Formatting
First things first, this is a dataset consisting of two halves in one. Be sure to use both datasets when looking at it. You're definitely going to need both in order to get the big picture. For your convenience, they are both in comma separated values (csv) which were manipulated using a program called OpenRefine as well as some code to get rid of impertinent information.

### How I Manipulated the Data
I used a simple code to change the first column (names) so that the individuals that were listed are not present. They were assigned basic numbers instead. If you're curious, I used this code: 

```import pandas as pd
df = pd.read_csv('csvfile')
uniques = df['column'].unique()
num = 0
for i in uniques:
    df.loc[df['column'] == i, ['column']] = num
    num += 1
#print(df.loc[df['column'] == "specificname"])
```

After that, I went into OpenRefine and made things a little more pretty: omitted unnecessary columns, created some Facets for easy manipulation, and collapsed the rest.

### Reuse Potential
This data should be used for statistics regarding the usage of reservations for the whole university even though this specific university has three campuses (the third doesn't have a reservation system). It can be used to look at duration of reservation, how often a room is being reserved over other rooms, as well as how often a particular user reserves rooms.

It's important to use both datasets together because even though there are two different locations, students, faculty, and staff from this university may migrate between the two campuses. This is because even though there are two campuses, they really work as one.

I would not recommend using this data to determine whether this university needs to stop doing or do more reservations. This is because there are some anomalies within the data. If a reservation is deleted or modified, that information is not reflected. Also, some staff are able to create reservations for other which could skew the user data if that staff member did not change the user. So, while there is an accurate account of how many reservation the user made, there is no guarantee that they made the reservation for someone else who also may have an account. Hope this helps and feel free to message me with any questions you may have about the dataset! 
