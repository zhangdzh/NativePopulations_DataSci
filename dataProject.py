import county_demographics
list_of_report = county_demographics.get_all_counties()
#populations/% ethniticites

countynames=[]
# for point in range(len(list_of_report)):
#     popdata = list_of_report[point]["County"]+",", list_of_report[point]["State"]+":", "\nPopulation 2014:",list_of_report[point]["Population"]["2014 Population"]
#     countyPop.append(popdata)

nativePercent=[]

state = input("What state would you like to see (enter abbreviation)? ").upper()

for point in range(len(list_of_report)):
    if list_of_report[point]["State"] == state:
        COUNTY = list_of_report[point]["County"]
        POP = list_of_report[point]["Ethnicities"]["American Indian and Alaska Native Alone"]
        countynames.append(COUNTY)
        nativePercent.append(POP)
# print(countynames)
# print(nativePercent)
# print(list_of_report[2380]["County"]+",", list_of_report[2380]["State"]+":")
# print(str(list_of_report[2380]["Ethnicities"]["American Indian and Alaska Native Alone"])+"%", "Native American/Alaskan Native Alone")

# for point in range(len(list_of_report)):
#     popdata = list_of_report[point]["County"]
#     countynames.append(popdata)
# for point in range(len(list_of_report)):
#     print(list_of_report[point]["County"]+",", list_of_report[point]["State"]+":")
#     print(str(list_of_report[point]["Ethnicities"]["American Indian and Alaska Native Alone"])+"%", "Native American/Alaskan Native Alone")
#     print(" ")

#interactive map
from bokeh.io import show
from bokeh.models import LogColorMapper
from bokeh.palettes import Viridis6 as palette
from bokeh.plotting import figure

from bokeh.sampledata.us_counties import data as counties
# from bokeh.sampledata.unemployment import data as unemployment

palette.reverse()

counties = {
    code: county for code, county in counties.items() if county["state"] == state.lower()
}

county_xs = [county["lons"] for county in counties.values()]
county_ys = [county["lats"] for county in counties.values()]

county_names = [countynames[county] for county in range(len(countynames))]
native_rates = [nativePercent[index] for index in range(len(countynames))]
color_mapper = LogColorMapper(palette=palette)

data=dict(
    x=county_xs,
    y=county_ys,
    name=county_names,
    rate=native_rates,
)

TOOLS = "pan,wheel_zoom,reset,hover,save"


#more actual stuff
p = figure(
    title="Native Populations in "+state.upper()+","+" 2014 (by county)", tools=TOOLS,
    x_axis_location=None, y_axis_location=None, plot_height=520, plot_width=810,
    tooltips=[
        ("Name", "@name"), ("Percentage of Population is Native", "@rate%"), ("(Long, Lat)", "($x, $y)")
    ])
p.grid.grid_line_color = None
p.hover.point_policy = "follow_mouse"

p.patches('x', 'y', source=data,
          fill_color={'field': 'rate', 'transform': color_mapper},
          fill_alpha=0.7, line_color="white", line_width=1)

show(p)
