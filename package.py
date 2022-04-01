import csv
import truck
from hash import ChainingHashTable


# Package class constructor
class Package:

    def __init__(self, id, address, city, state, zip, deadline, weight, note, start, time_at_location, delivered_time):
        self.ID = id
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.weight = weight
        self.note = note
        self.start = start
        self.location = time_at_location
        self.status = delivered_time

    def __str__(self):  # overwrite print(Package) otherwise it will print object reference
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s" % (
            self.ID, self.address, self.city, self.state, self.zip, self.deadline, self.weight, self.note, self.start,
            self.location, self.status)


def load_package_data(filename):
    with open(filename) as package_file:
        package_data = csv.reader(package_file, delimiter=',')
        next(package_data)  # skip header
        for p in package_data:
            p_id = int(p[0])
            p_address = p[1]
            p_city = p[2]
            p_state = p[3]
            p_zip = p[4]
            p_deadline = p[5]
            p_weight = p[6]
            p_note = p[7]
            p_start = p[8]
            p_location = p[9]
            p_status = p[10]

            if p_deadline == '9:00 AM':
                truck.truck1.insert(p)

            if p_deadline == '10:30 AM' and p_note != 'Delayed on flight':
                truck.truck1.insert(p)

            if p_deadline == 'EOD' and p_zip == '84104' and p_address == '2010 W 500 S':
                truck.truck1.insert(p)

            # Second truck's delivery
            if p_deadline == '10:30 AM' and p_note == 'Delayed on flight':
                truck.truck2.insert(p)

            # First truck's first delivery
            if p_deadline == 'EOD' and p_note == 'Can only be on truck 2':
                truck.truck2.insert(p)

            if p_deadline == 'EOD' and p_zip == '84119' and p_note != 'Can only be on truck 2':
                truck.truck3.insert(p)

            if p_deadline == 'EOD' and p_note == 'Wrong address listed':
                p[1] = '410 S State St'
                p[4] = '84111'
                truck.truck2.insert(p)

            if p_deadline == 'EOD' and p_zip == '84106':
                truck.truck3.insert(p)

            if p_deadline == 'EOD' and p_zip == '84115':
                truck.truck3.insert(p)

            # # Correct incorrect package details
            if p not in truck.truck1.packages_loaded and p not in truck.truck2.packages_loaded and p not in truck.truck3.packages_loaded:
                if len(truck.truck2.packages_loaded) < 12:
                    truck.truck2.insert(p)
                elif len(truck.truck3.packages_loaded) < 15:
                    truck.truck3.insert(p)
                else:
                    print("package could not be loaded", p_id)

            # p object p = Package(p_id, p_address, p_city, p_state, p_zip, p_deadline, p_weight, p_note, p_start,
            # p_location, p_status)

            # insert it into the hash table
            package_hash.insert(p_id, p)


# Hash table instance
package_hash = ChainingHashTable()

# Load packages to Hash Table
load_package_data('package.csv')


def get_package():
    print("Packages from Hashtable:")
    # Fetch data from Hash Table
    for i in range(len(package_hash.table) + 1):
        print("Package: {}".format(package_hash.search(i + 1)))  # 1 to 11 is sent to myHash.search()


def search_package(p_id):
    result = package_hash.search(p_id)
    print(result)
