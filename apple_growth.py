def simulate_apple_growth(
    sun_intensity,
    initial_size,
    initial_mass,
    ripening_threshold,
    falling_threshold,
    time_steps,
):
    # Initialize variables
    apple_size = initial_size
    apple_mass = initial_mass
    position_y = 1  # Assume initial position is 1 (on the tree)
    ripening_status = False

    # Lists to store simulation results
    process_data = []

    for step in range(time_steps):
        # Update apple size and mass based on photosynthesis (simplified model)
        apple_size += sun_intensity * 0.1  # Simplified growth rate
        apple_mass += sun_intensity * 0.05  # Simplified mass increase

        # Check for ripening
        if apple_mass >= ripening_threshold and not ripening_status:
            ripening_status = True

        # Check if the apple should fall
        if apple_mass >= falling_threshold:
            position_y = 0  # Apple falls to the ground

        # Record the state for this time step
        process_data.append(
            {
                "size": apple_size,
                "mass": apple_mass,
                "position_y": position_y,
                "ripening_status": ripening_status,
            }
        )

    return process_data


# Define simulation parameters
sun_intensity = 5  # Constant sun intensity
initial_size = 1  # Initial apple size
initial_mass = 0.5  # Initial apple mass
ripening_threshold = 2  # Mass threshold for ripening
falling_threshold = 3  # Mass threshold for falling
time_steps = 10  # Number of time steps

# Run the simulation
process_data = simulate_apple_growth(
    sun_intensity,
    initial_size,
    initial_mass,
    ripening_threshold,
    falling_threshold,
    time_steps,
)

process_data

# fall = change position_y from 1 to 0
# ripening = change ripe from False to True
# growing = increase of size

# does apple grow? growth data -> detect pattern of size increasing
# does apple becomes ripe? growth data -> detect pattern of ripe changing
# does apple fall down in the end? growth data -> detect pattern of pos_y changing

# does apple grow without sun? growth data when sun intensity = 0 -> detect pattern of size increasing
# does apple fall without ripe?  growth data when sun ripe not changing -> detect pattern of changing pos y
# how much apple grow in 2 days? calc size changing in 2 steps


def is_attribute_increasing(process_data):
    return any(step["size"] < process_data[-1]["size"] for step in process_data)


def is_attribute_changes(process_data, attribute, from_value, to_value):
    previous_value = None

    for item in process_data:
        current_value = item.get(attribute)
        if current_value == to_value and previous_value == from_value:
            return True
        previous_value = current_value

    return False


def does_apple_fall_down(process_data):
    return any(step["position_y"] == 0 for step in process_data)


def grow_rate(process_data, days):
    if len(process_data) >= days:
        return process_data[days - 1]["size"] - process_data[0]["size"]
    else:
        return 0


apple_grows = is_attribute_increasing(process_data)
apple_ripens = is_attribute_changes(process_data, "ripening_status", False, True)
apple_falls = is_attribute_changes(process_data, "position_y", 1, 0)
growth_in_2_days = grow_rate(process_data, 2)

(apple_grows, apple_ripens, apple_falls, growth_in_2_days)
