import pandas as pd
import matplotlib.pyplot as plt
from pandas.core import tools

# Data provided
data = {
    "Pledge year": [
        "Spring 2002", "Spring 2002", "Spring 2003", "Spring 2003", "Spring 2003", "Spring 2003",
        "Spring 2003", "Spring 2003", "Spring 2003", "Spring 2004", "Spring 2004", "Spring 2005",
        "Spring 2005", "Spring 2006", "Spring 2006", "Spring 2006", "Spring 2006", "Spring 2006",
        "Spring 2008", "Fall 2008", "Fall 2008", "Spring 2012", "Spring 2012", "Spring 2013",
        "Fall 2015", "Fall 2015", "Fall 2015", "Fall 2015", "Fall 2015", "Fall 2015", "Fall 2018",
        "Fall 2018", "Fall 2018", "Fall 2021", "Fall 2021", "Fall 2021", "Spring 2022", "Spring 2022",
        "Spring 2023", "Spring 2023", "Spring 2023", "Spring 2024", "Spring 2024",
        "Fall 2024", "Fall 2024", "Fall 2024",
        # insert new pledge year here
    ],
    "Line Names": [
        "Two Beans in a Bucket", "Two Beans in a Bucket", "Daniels Line", "Daniels Line",
        "Daniels Line", "Daniels Line", "Daniels Line", "Daniels Line", "Daniels Line",
        "Qtinuation", "Qtinuation", "Soldiers of Discretion", "Soldiers of Discretion",
        "Purple Haze", "Purple Haze", "Purple Haze", "Purple Haze", "Purple Haze",
        "Last Man Standing", "Ying Yang Twinz", "Ying Yang Twinz", "Quelateral Damages",
        "Quelateral Damages", "Single Shot at Destiny", "V6 Ride or Die", "V6 Ride or Die",
        "V6 Ride or Die", "V6 Ride or Die", "V6 Ride or Die", "V6 Ride or Die", "3 The Hard Way",
        "3 The Hard Way", "3 The Hard Way", "Da Bomb Squad", "Da Bomb Squad", "Da Bomb Squad",
        "Two Queribbean Souls", "Two Queribbean Souls", "The Aftermath 3", "The Aftermath 3",
        "The Aftermath 3", "Two Sons of Tenacity", "Two Sons of Tenacity"
        # Insert new Line names here
    ],
    "Sons of ALL": [
        "Andre \"Luther V\" Pippen", "Jimmy \"Colorblind\" Wanzer", "Frinso Padivill", "Tyque McCarthy",
        "Berket Godsey", "Norris Goode", "Gerry Washington", "Damion Pressor", "Patrick Ellerby",
        "Gary “Scrappy” Williams", "Rod “Scooby Doo” Jimil Barris", "Malek “Movie Star” Crawford",
        "Elliot “Harlem Shaq” Thweatt", "Ralph Rogers", "Lucky O'Connor", "Robert Tolbert",
        "Stephen Corsey", "Tion Johnson", "Curtis \"Hollywood\" Giles", "Levar \"Uncle Rucques\" Jordan",
        "Sekou \"Hancock\" Oney", "Dwayne \"Black Ops\" Lockett", "Billy \"Blackowt\" Anderson",
        "Irving \"Wheezy\" Duhart", "Treance \"The Kid\" Hobbs", "Keith \"Easy\" Jones",
        "James \"Get Smart\" Greene Jr.", "Paul \"Shotgun\" Flemings", "Larnell \"Charge\" Simpson Jr.",
        "Demayne \"Shake\" Collins", "Andrew “QueHeffner” Rollins", "Brian “EQuefax” Smith",
        "Darryl “BlackQuelightning” McGuire", "Dr. Nathaniel “Time Bomb” Mizzell",
        "Johnny “Short Fuse” Fleetwood", "Pattrezzes “Live Wire” Myles Sr.", "Levi \"Passport\" Davis",
        "Pierre \"Top Flight\" Saint Louis", "Gregory “Slim Shaddy” Powers", "Maurice “Bizaar” Hill",
        "Tracy “Cool Breeze” White", "Taj “Radio” Weems", "Camren “A-Track” McKinney",
        # Add new names here
    ]
}

# Creating the DataFrame
df = pd.DataFrame(data)


# Custom sorting function
def sort_key(pledge_year):
    season, year = pledge_year.split()
    return int(year), 0 if season == 'Spring' else 1


# Grouping and sorting the DataFrame
formatted_df = df.groupby(["Pledge year", "Line Names"])["Sons of ALL"].apply(lambda x: ', '.join(x)).reset_index()
formatted_df["sort_key"] = formatted_df["Pledge year"].apply(sort_key)
sorted_df = formatted_df.sort_values(by="sort_key").drop(columns="sort_key").reset_index(drop=True)

# Display the sorted DataFrame
tools.display_dataframe_to_user(name="Sorted Pledge Year Data", dataframe=sorted_df)

print(sorted_df.to_string())
