#   Helyanny Perozo
#   Your Student ID:216238389 
import math

#   The first part of this program will calculate 
#   the cost of the rocket to build (Rocket Design)

#   Constants
FEET_PER_METER = 3.28
DENSITY = 1.225
LOWER_MASS_ROCKET = 100000
HIGHER_MASS_ROCKET = 400000
FUEL_UNDER_100000 = 1360
FUEL_UNDER_400000 = 2000
FUEL_400000_ABOVE = 2721
COST_MATERIALS = 5
COST_FUEL = 6.1
TAX = 15
MAX_WEIGHT_ITEMS = 5/100
MIN_WEIGHT_BOX = 20
MAX_WEIGHT_BOX = 500
MAX_STORAGE_VOLUME = 40/100
MIN_VOLUME_BOX = 0.125
GRAVITY = 9.81

#   Function that converts feet to meters
def feet_to_meter(length) :
    """ 
    (float) -> float
    Returns the given length from feet to meters
    (rounded to 2 decimals)
    >>> feet_to_meter(5.0)
    1.52
    >>> feet_to_meter(43.76)
    13.34
    >>> feet_to_meter(22.48)
    6.85
    """
    length_in_meters = length / FEET_PER_METER
    return round(length_in_meters, 2)

#   Function that calculates the rocket volume
def rocket_volume(radius, height_cone, height_cyl) :
    """
    (float, float, float) -> float
    Returns the volume of the rocket in cube meters
    (rounded to 2 decimals)
    >>> rocket_volume(13.4, 17.6, 3.9)
    5509.42
    >>> rocket_volume(14.7, 25.6, 42.9)
    34916.38
    >>> rocket_volume(21.1, 32.4, 8.9)
    27553.77
    """
    area_circle = math.pi * radius ** 2
    volume_cone = area_circle * height_cone /  3
    volume_cyl = area_circle * height_cyl
    volume_rocket = volume_cone + volume_cyl
    return round(volume_rocket, 2)

#   Function that calculates the rocket surface area
def rocket_area(radius, height_cone, height_cyl) :
    """
    (float, float, float) -> float
    Returns the area of the rocket in square meters
    (rounded to 2 decimals)
    >>> rocket_area(2.0, 7.0, 3.0)
    96.01
    >>> rocket_area(31.7, 17.8, 3.4)
    7454.76
    >>> rocket_area(5.7, 12.9, 7.3)
    616.06
    """
    area_circle = math.pi * radius ** 2
    area_cone = math.pi * radius * (radius + \
    math.sqrt(height_cone ** 2 + radius ** 2))
    area_cyl = 2 * math.pi * radius * (height_cyl + radius)
    area_rocket = area_cone + area_cyl - 2 * area_circle
    return round(area_rocket, 2)

#   Function that calculates the rocket mass
def rocket_mass(radius, height_cone, height_cyl) :
    """
    (float, float, float) -> float
    Returns the total mass of the rocket in kg
    (rounded to 2 decimals)
    >>> rocket_mass(13.4, 17.6, 3.9)
    6749.04
    >>> rocket_mass(3.4, 5.8, 11.9)
    615.42
    >>> rocket_mass(7.5, 22.6, 8.0)
    3362.59
    """
    mass_rocket = rocket_volume(radius, height_cone, height_cyl) \
                  * DENSITY
    return round(mass_rocket, 2)

#   Function that calculates the amount of fuel for the rocket
def rocket_fuel(radius, height_cone, height_cyl, velocity_e, velocity_i, time) :
    """
    (float, float, float, float, float, float) -> float
    Returns the total fuel needed for the rocket in kg
    (rounded to 2 decimals)
    >>> rocket_fuel(50.0, 100.0, 800.0, 700.0, 300.0, 120.0)
    4616444.53
    >>> rocket_fuel(10.0, 10.0, 10.0, 700.0, 300.0, 120.0)
    165945.55
    >>> rocket_fuel(32.6, 23.4, 17.8, 700.0, 300.0, 120.0)
    296022.96
    """
    fuel_rocket = rocket_mass(radius, height_cone, height_cyl) * (math.e ** (velocity_i / velocity_e) - 1)
    if rocket_mass(radius, height_cone, height_cyl) < LOWER_MASS_ROCKET :
        burnt_fuel = FUEL_UNDER_100000 * time
    elif rocket_mass(radius, height_cone, height_cyl) >= LOWER_MASS_ROCKET \
         and rocket_mass(radius, height_cone, height_cyl) < HIGHER_MASS_ROCKET :
        burnt_fuel = FUEL_UNDER_400000 * time
    else :
        burnt_fuel = FUEL_400000_ABOVE * time
    total_fuel = burnt_fuel + fuel_rocket
    return round(total_fuel, 2)

#   This function calculates the cost of the rocket
def calculate_cost(radius, height_cone, height_cyl, velocity_e, velocity_i, time, tax) :
    """
    (float, float, float, float, float, float, boolean) -> float
    Returns the approximate total cost to build rocket
    (rounded to 2 decimals)
    >>> calculate_cost(50.0, 100.0, 800.0, 700.0, 300.0, 120.0, False)
    29544028.78
    >>> calculate_cost(27.7, 124.1, 311.1, 700.0, 85.5, 112.3, True)
    3480914.15
    >>> calculate_cost(81.3, 74.6, 200.0, 502.3, 83.9, 200.0, False)
    10418196.05
    """
    cost_materials = rocket_area(radius, height_cone, height_cyl) * COST_MATERIALS
    cost_fuel = rocket_fuel(radius, height_cone, height_cyl, velocity_e, velocity_i, time) * COST_FUEL
    pretax_cost = cost_materials + cost_fuel
    if tax == True :
        total_cost = pretax_cost * (100 + TAX) / 100
    else :
        total_cost = pretax_cost
    return round(total_cost, 2)

#   The second part of this program will test out 
#   the rocket simulation
def compute_storage_space(radius, height_cyl) :
    """
    (float, float) -> float, float, float
    Returns the dimensions of the storage box
    (rounded to 2 decimals)
    >>> compute_storage_space(5.0, 10.0)
    (7.07, 7.07, 5.0)
    >>> compute_storage_space(13.7, 52.2)
    (19.37, 19.37, 26.1)
    >>> compute_storage_space(7.5, 31.9)
    (10.61, 10.61, 15.95)
    """
    length_rocket = width_rocket = round(math.sqrt(2) * radius, 2)
    height_rocket = round(height_cyl / 2, 2)
    return width_rocket, length_rocket, height_rocket

#   This function simulates the transportation of equipment
def load_rocket(mass_rocket, radius, height_cyl) :
    """
    (float, float, float) -> float
    """
    width_rocket, length_rocket, height_rocket = compute_storage_space(radius, height_cyl)
    volume_storage = width_rocket * length_rocket * height_rocket
    max_weight_storage = mass_rocket * MAX_WEIGHT_ITEMS
    max_volume_storage = width_rocket * length_rocket * height_rocket * MAX_STORAGE_VOLUME
    if max_weight_storage < MIN_WEIGHT_BOX or volume_storage < MIN_VOLUME_BOX :
        print("No more items can be added")
        return mass_rocket
    else:
        item_weight = input("Please enter the weight of the next item (type \"Done\" when you are done filling the rocket) : ")
        item_width = float(input("Enter item width : "))
        item_length = float(input("Enter item length : "))
        item_height = float(input("Enter item height : "))
        volume_item = item_width * item_length * item_height
        a = "Item could not be added... please try again..."
        end = 'Done'
        if item_weight == end :
            print("No more items can be added")
        elif float(item_weight) > max_weight_storage or float(item_weight) > MAX_WEIGHT_BOX or float(item_weight) < MIN_WEIGHT_BOX :
            print(a)
        elif volume_item > max_volume_storage or volume_item < MIN_VOLUME_BOX :
            print(a)
        else :
            while float(item_weight) <= max_weight_storage and volume_item <= max_volume_storage :
                item_weight += item_weight
                volume_item += volume_item
    updated_weight = mass_rocket + item_weight
    return updated_weight

#part 9

#part 10
    