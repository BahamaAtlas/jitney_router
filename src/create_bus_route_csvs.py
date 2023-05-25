import csv

def create_bus_route_csvs(pdf_text):
    # Split the text into individual routes
    routes = pdf_text.split("Route #")[1:]

    # Iterate over each route
    for route in routes:
        # Extract the service area
        service_area = route.split('\n')[0].strip()

        # Extract the route number and starting point
        route_info = route.split('\n')[1].strip().split(' ')
        route_number = route_info[0]
        starting_point = ' '.join(route_info[2:])

        # Extract the street names
        street_names = route.split('\n')[2].split('/')
        street_names = [name.strip() for name in street_names]

        # Create a new CSV file for the route
        csv_filename = f'Route_{route_number}.csv'
        with open(csv_filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Service Area', 'Route Number', 'Starting Point', 'Street Names'])
            writer.writerow([service_area, route_number, starting_point, '/'.join(street_names)])

        print(f'Created CSV file for Route {route_number}')

# Example usage
pdf_text = """
Official Bus Routes

Englerston
Route #1 Starting Point: East Hill Street
Street 1/Street 2/Street 3

Downtown
Route #2 Starting Point: Main Street
Street 4/Street 5/Street 6
"""

create_bus_route_csvs(pdf_text)
