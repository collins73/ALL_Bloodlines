"""
This portion of the code will be used for all updates from the main python master file.
I can also display a simple bar chart visualization for all successive pledge lines from
the past to the present...

"""

import pandas as pd
import matplotlib.pyplot as plt
from pandas.core import tools

from ALL_Bloodlines import df, sort_key

# ... (Your existing data and code remain the same) ...

# Count pledges per year
pledge_counts = df["Pledge year"].value_counts().sort_index()

# Custom sorting function for pledge years (same as before)
# ...

# Apply sorting to pledge counts
pledge_counts.index = pledge_counts.index.map(sort_key)
pledge_counts = pledge_counts.sort_index()

# Visualization with Matplotlib
plt.figure(figsize=(10, 6))  # Adjust figure size as needed
pledge_counts.plot(kind='bar')
plt.title('Number of Pledges per Year')
plt.xlabel('Pledge Year')
plt.ylabel('Number of Pledges')
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.show()