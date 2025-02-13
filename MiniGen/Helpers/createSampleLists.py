""" Script to create some sample data"""
from pathlib import Path

words = [
    "Acorn", "Adventure", "Anchor", "Angel", "Apricot", "Arch", "Arrow", "Artist", "Ash", "Asphalt", "Astronaut", "Atlas", "Atom", "Avenue", "Avocado", "Baby", "Backpack", "Bakery", "Bamboo", "Band", "Banner", "Barbecue", "Barn", "Barrel", "Beach", "Bead", "Beam", "Bear", "Beetle", "Bell", "Berry", "Bicycle", "Bill", "Birch", "Biscuit", "Blanket", "Blizzard", "Blossom", "Blueprint", "Board", "Boat", "Bonfire", "Book", "Bottle", "Bouquet", "Bow", "Bowl", "Box", "Bracelet", "Brain", "Branch", "Bread", "Breeze", "Brick", "Bridge", "Broccoli", "Brush", "Bubble", "Bucket", "Buffalo", "Bug", "Building", "Bulb", "Bumper", "Bungalow", "Bunker", "Butterfly", "Button", "Cactus", "Cake", "Calculator", "Calendar", "Camel", "Camera", "Camp", "Candle", "Canoe", "Canvas", "Canyon", "Cape", "Caramel", "Carnival", "Carpet", "Cart", "Castle", "Caterpillar", "Cave", "Cedar", "Ceiling", "Cell", "Cement", "Centaur", "Chain", "Chair", "Chalk", "Champion", "Chapel", "Charcoal", "Chart", "Check", "Cheese", "Cherry", "Chest", "Chicken", "Chimney", "Chocolate", "Chord", "Circle", "Circus", "Cliff", "Clock", "Cloud", "Clover", "Coach", "Coal", "Coast", "Coconut", "Coin", "Collar", "Comet", "Compass", "Concert", "Cone", "Coral", "Cork", "Corn", "Cottage", "Cotton", "Couch", "Crab", "Crane", "Crayon", "Creek", "Cricket", "Crocodile", "Crown", "Crystal", "Cup", "Curtain", "Cushion", "Daffodil", "Daisy", "Dance", "Dawn", "Deer", "Desert", "Diamond", "Dinosaur", "Disco", "Dolphin", "Donkey", "Doorbell", "Dragon", "Drawer", "Dream", "Dress", "Drill", "Duck", "Dust", "Eagle", "Earth", "Echo", "Eclipse", "Elf", "Engine", "Envelope", "Falcon", "Fan", "Feather", "Fence", "Festival", "Field", "Firefly", "Flag", "Flute", "Fog", "Forest", "Fountain", "Fox", "Frame", "Frog", "Galaxy", "Garage", "Gardenia", "Gate", "Gem", "Ghost", "Glacier", "Globe", "Goat", "Gold", "Goose", "Grapes", "Grasshopper", "Guitar", "Gym", "Harbor", "Harmony", "Harvest", "Hedge", "Helmet", "Hill", "Hive", "Horizon", "Hurricane", "Iceberg", "Igloo", "Ink", "Insect", "Island", "Ivory", "Ivy", "Jacket", "Jaguar", "Jelly", "Jewel", "Journey", "Jungle", "Kangaroo", "Kayak", "Kettle", "King", "Kitten", "Kiwi", "Knight", "Koala", "Lab", "Ladder", "Lake", "Lantern", "Lava", "Leaf", "Library", "Lighthouse", "Lily", "Lion", "Lizard", "Log", "Luggage", "Lumber", "Machine", "Magnet", "Mansion", "Maple", "Marsh", "Meadow", "Melon", "Meteor", "Microphone", "Milk", "Mill", "Mist", "Monkey", "Moonlight", "Moss", "Mountain", "Mouse", "Mushroom", "Music", "Mustard", "Mystery", "Nest", "Nightingale", "North", "Nutmeg", "Oak", "Oasis", "Ocean", "Octagon", "Olive", "Onion", "Opera", "Orchid", "Owl", "Oyster", "Palace", "Panda", "Parachute", "Parrot", "Path", "Peach", "Peacock", "Peanut", "Pebble", "Pelican", "Penguin", "Pepper", "Petal", "Phoenix", "Piano", "Picnic", "Pine", "Planet", "Plum", "Pond", "Popcorn", "Porch", "Prairie", "Prism", "Pumpkin", "Pyramid", "Quail", "Quartz", "Quicksand", "Quilt", "Rabbit", "Radar", "Rainbow", "Ranch", "Raven", "Reef", "Ribbon", "River", "Road", "Robot", "Rocket", "Rose", "Ruby", "Saddle", "Sail", "Sand", "Satellite", "Scarf", "School", "Scorpion", "Sculpture", "Sea", "Seahorse", "Seal", "Seed", "Shadow", "Shark", "Sheep", "Shell", "Shield", "Ship", "Shore", "Shrub", "Silk", "Silver", "Skate", "Skeleton", "Sky", "Sled", "Sloth", "Smoke", "Snow", "Soap", "Solar", "Song", "Sparrow", "Sphere", "Spider", "Spiral", "Spoon", "Spring", "Sprout", "Square", "Squirrel", "Stage", "Starfish", "Statue", "Steam", "Stone", "Storm", "Stream", "Street", "Sunflower", "Surf", "Swamp", "Swan", "Swing", "Sword", "Symphony", "Table", "Tapestry", "Telescope", "Temple", "Tent", "Thistle", "Thorn", "Thunder", "Tiger", "Toad", "Tomato", "Tower", "Trail", "Train", "Treasure", "Treehouse", "Triangle", "Trout", "Tulip", "Tunnel", "Turtle", "Twig", "Unicorn", "Valley", "Vase", "Velvet", "Vine", "Volcano", "Wagon", "Walnut", "Waterfall", "Wave", "Whale", "Wheel", "Willow", "Wind", "Window", "Wing", "Wolf", "Wood", "Wreath", "Yacht", "Yard", "Yarn", "Zebra", "Zenith", "Zipper", "Zone", "Zoo","Accordion", "Acrobat", "Acrylic", "Aisle", "Alchemy", "Algae", "Almond", "Alpaca", "Altitude", "Amber", "Ambulance", "Amethyst", "Amphibian", "Anchor", "Anemone", "Angler", "Antelope", "Anthem", "Antique", "Anvil", "Apron", "Aquarium", "Arcade", "Archery", "Arctic", "Arena", "Argyle", "Armada", "Armchair", "Arrowhead", "Artifact", "Artisan", "Asparagus", "Asteroid", "Astronomy", "Atlas", "Atmosphere", "Attic", "Aurora", "Autumn", "Avalanche", "Avenue", "Aviary", "Avocado", "Axle", "Baboon", "Backyard", "Bacon", "Badge", "Badger", "Baggage", "Baker", "Bakery", "Balcony", "Balloon", "Bamboo", "Banana", "Bandana", "Banjo", "Barbecue", "Barista", "Barnacle", "Barracuda", "Barrel", "Baseball", "Basketball", "Basil", "Bassoon", "Baton", "Bazaar", "Beacon", "Beagle", "Beanstalk", "Beaver", "Bedrock", "Beehive", "Beetle", "Bellflower", "Belltower", "Bench", "Bicycle", "Billiards", "Binoculars", "Biplane", "Birdhouse", "Birthday", "Bison", "Blackberry", "Blacksmith", "Blender", "Blizzard", "Blueprint", "Boardwalk", "Boathouse", "Bobcat", "Bobsled", "Bodyguard", "Bohemian", "Bookmark", "Boomerang", "Boulevard", "Bowling", "Boxcar", "Bracelet", "Brainstorm", "Brass", "Breadstick", "Bricklayer", "Bridge", "Broccoli", "Broomstick", "Bubblegum", "Buckaroo", "Buffet", "Bulldozer", "Bulletin", "Bumblebee", "Bungalow", "Burglar", "Bushel", "Buttercup", "Butterfly", "Butterscotch", "Cabin", "Cactus", "Cafeteria", "Calamity", "Calculator", "Calendar", "Camel", "Campfire", "Campsite", "Canary", "Candlelight", "Candy", "Canoe", "Canvas", "Canyon", "Capricorn", "Carousel", "Carpenter", "Carrot", "Cartwheel", "Cascade", "Cashmere", "Catamaran", "Caterpillar", "Cathedral", "Cauldron", "Cavalry", "Cedar", "Celery", "Cellar", "Centipede", "Ceramic", "Chameleon", "Chandelier", "Chariot", "Cheesecake", "Cherry", "Chessboard", "Chickadee", "Chimney", "Chisel", "Chocolate", "Chrysanthemum", "Cinnamon", "Circus", "Clamshell", "Clarinet", "Cliffside", "Climber", "Clover", "Coastline", "Coconut", "Coffin", "Colander", "Coliseum", "Compass", "Compost", "Concert", "Conductor", "Conifer", "Constellation", "Continent", "Coral", "Cornfield", "Cornucopia", "Costume", "Cottage", "Cottonwood", "Countryside", "Courtyard", "Coyote", "Crabapple", "Cradle", "Crater", "Crayfish", "Creamery", "Cricket", "Crocodile", "Crossbow", "Crowbar", "Cucumber", "Cupcake", "Curtain", "Cyclone", "Daffodil", "Dandelion", "Dartboard", "Daydream", "Daylight", "Deer", "Delight", "Desert", "Dessert", "Diamond", "Dinosaur", "Diorama", "Dolphin", "Domino", "Doorway", "Dragonfly", "Driftwood", "Drumstick", "Duckling", "Dune", "Dusk", "Dustpan", "Eagle", "Easel", "Eclipse", "Eel", "Eggplant", "Elderberry", "Elephant", "Elevator", "Elm", "Emerald", "Emperor", "Encyclopedia", "Endeavor", "Engine", "Equator", "Equinox", "Eucalyptus", "Euphonium", "Evergreen", "Exhibit", "Falcon", "Fanfare", "Farmhouse", "Feather", "Ferris", "Fiddle", "Fireplace", "Firewood", "Fishbowl", "Flagpole", "Flamingo", "Flashlight", "Flock", "Flour", "Flowerpot", "Flute", "Fog", "Foliage", "Footbridge", "Footprint", "Forest", "Fortress", "Fossil", "Fountain", "Foxglove", "Fragrance", "Freight", "Frost", "Frostbite", "Fruitcake", "Furnace", "Galaxy", "Galleon", "Garnet", "Gazebo", "Gecko", "Geode", "Geyser", "Gingerbread", "Giraffe", "Glacier", "Gladiator", "Glider", "Glitter", "Gondola", "Gooseberry", "Gopher", "Gorilla", "Gourd", "Grapevine", "Greenhouse", "Grotto", "Guitar", "Gull", "Gumdrop", "Guppy", "Gust", "Gyroscope", "Hailstorm", "Halibut", "Hamster", "Harbor", "Harmonica", "Harvest", "Haystack", "Hazelnut", "Helicopter", "Hibiscus", "Highway", "Hillside", "Hippopotamus", "Horizon", "Horseback", "Hotdog", "Hummingbird", "Hurricane", "Hydrangea", "Icicle", "Igloo", "Illusion", "Incense", "Inkwell", "Inlet", "Insect", "Iris", "Ironwood", "Island", "Ivory", "Jackal", "Jackrabbit", "Jamboree", "Jasmine", "Javelin", "Jellybean", "Jigsaw", "Jubilee", "Jukebox", "Jungle", "Jupiter", "Kaleidoscope", "Kangaroo", "Kayak", "Keepsake", "Kettle", "Kite", "Kiwi", "Knapsack", "Knothole", "Labyrinth", "Ladder", "Lagoon", "Lamb", "Lantern", "Lark", "Lasso", "Lattice", "Lavender", "Lawnmower", "Lemonade", "Lighthouse", "Lilac", "Lily", "Limestone", "Lobster", "Locomotive", "Lollipop", "Lumberjack", "Lynx", "Macaroni", "Mackerel", "Magnolia", "Mahogany", "Mailbox", "Mammoth", "Mandolin", "Mango", "Maple", "Marigold", "Marina", "Marionette", "Marshmallow", "Meadow", "Meerkat", "Melody", "Mermaid", "Meteor", "Millipede", "Minivan", "Mistletoe", "Mockingbird", "Monarch", "Monastery", "Monsoon", "Moonbeam", "Moonstone", "Morning", "Mosaic", "Mosquito", "Mountain", "Mushroom", "Music", "Mustang", "Mystery", "Nectarine", "Needle", "Nest", "Nightfall", "Nightingale", "Nimbus", "Noodle", "North", "Nostalgia", "Notebook", "Nutcracker", "Oak", "Oasis", "Obelisk", "Octopus", "Olive", "Onyx", "Opal", "Orangutan", "Orchid", "Oregano", "Origami", "Oriole", "Ostrich", "Otter", "Outback", "Outpost", "Owl", "Oxen", "Oyster", "Paddle", "Pagoda", "Paintbrush", "Palace", "Palm", "Panorama", "Papaya", "Parachute", "Parade", "Parakeet", "Parasol", "Parsnip", "Passage", "Passionfruit", "Pathway", "Peacock", "Peanut", "Pearl", "Pebble", "Pelican", "Peppermint", "Periscope", "Petunia", "Phantom", "Phoenix", "Piano", "Picnic", "Pineapple", "Pioneer", "Pirate", "Pistachio", "Pitcher", "Pixie", "Plankton", "Platinum", "Plow", "Plum", "Pluto", "Pomegranate"]

first_names = [
    "Stacey", "Karen", "Jason", "Angela", "Amber", "Samantha", "Bradley", "Daniel", "Justin", "Rebecca",
    "Brian", "Steven", "Lacey", "Laurie", "Joshua", "Nathan", "Michele", "Robert", "Jennifer", "Joseph",
    "Mary", "Donald", "Cynthia", "Ashley", "Jessica", "Jordan", "Gerald", "John", "Kathleen", "Clayton",
    "Sara", "Scott", "Andrea", "Alex", "James", "Elizabeth", "Jamie", "Michael", "Stephanie", "Rachel",
    "Thomas", "Martha", "Christina", "Amy", "Gabrielle", "Gregory", "Tracy", "Timothy", "Sherri", "Pamela",
    "Jacob", "Jill", "Dana", "Dorothy", "Richard", "Troy", "Jackie", "Victoria", "Kenneth", "Mindy",
    "Chad", "Aaron", "Curtis", "Ana", "Danielle", "Chloe", "David", "Matthew", "Kevin", "Juan",
    "Brenda", "Melissa", "Colton", "Raymond", "Allison", "Deanna", "Hayley", "Joel", "Toni", "Eric",
    "Holly", "Carrie", "Ryan", "Lindsay", "Dustin", "Robin", "Maurice", "Cassandra", "Adam", "Kelly",
    "Austin", "Andrew", "Anna", "Craig", "Kara", "Samuel", "Diana", "Rodney", "Gene", "Carmen",
    "Walter", "Christian", "Wanda", "Seth", "Casey", "Alejandra", "William", "Lee", "Tanya", "Marissa",
    "Darrell", "Erik", "Alicia", "Anthony", "Katie", "Sarah", "Jade", "Alyssa", "Tony", "George",
    "Jeffrey", "Amanda", "Regina", "Arthur", "Heidi", "Martin", "Emily", "Jaclyn", "Paul", "Michelle",
    "Lisa", "Tina", "Nicholas", "Calvin", "Shannon", "Lori", "Sonya", "Katrina", "Todd", "Donna",
    "Keith", "Tyler", "Veronica", "Laura", "Kristin", "Catherine", "Kathy", "Daisy", "Miranda", "Cameron",
    "Crystal", "Derrick", "Bobby", "Krystal", "Tamara", "Alexandria", "Mark", "Linda", "Misty", "Jeff",
    "Terry", "Gary", "April", "Brandi", "Stephen", "Sydney", "Jacqueline", "Alexandra", "Ronald", "Erin",
    "Henry", "Teresa", "Dominique", "Theresa", "Yolanda", "Grace", "Brittany", "Patricia", "Janet", "Christine",
    "Adrian", "Heather", "Wendy", "Joe", "Tiffany", "Jasmine", "Cristian", "Paige", "Darren", "Kristen",
    "Angelica", "Angie", "Rachael", "Ruben", "Joyce", "Kimberly", "Mike", "Tammy", "Jeremy", "Dylan",
    "Johnathan", "Kristina", "Mitchell", "Carlos", "Madeline", "Frank", "Kaitlin", "Renee", "Nancy", "Jenny",
    "Lance", "Paula", "Travis", "Claire", "Alec", "Gabriel", "Margaret", "Carla", "Suzanne", "Aimee",
    "Douglas", "Taylor", "Diane", "Meredith", "Megan", "Courtney", "Jonathan", "Shawn", "Larry", "Emma",
    "Bryan", "Anita", "Trevor", "Kim", "Theodore", "Gina", "Sylvia", "Luis", "Charlotte", "Carol",
    "Jon", "Oscar", "Mariah", "Perry", "Jack", "Devon", "Susan", "Deborah", "Natalie", "Maxwell",
    "Felicia", "Charles", "Stacy", "Jesse", "Derek", "Christopher", "Rickey", "Natasha", "Darryl", "Kristy",
    "Dennis", "Caitlyn", "Mikayla", "Bridget", "Peter", "Joanna", "Cheryl", "Shari", "Shelly", "Kathryn",
    "Corey", "Judy", "Evan", "Steve", "Denise", "Ashlee", "Hannah", "Anne", "Brandon", "Victor",
    "Lauren", "Jonathon", "Julia", "Angel", "Tyrone", "Chelsea", "Eduardo", "Roger", "Darin", "Kirk",
    "Barry", "Evelyn", "Beverly", "Sandra", "Sherry", "Erica", "Luke", "Melinda", "Brooke", "Cheyenne",
    "Bonnie", "Greg", "Marcia", "Whitney", "Savannah", "Jerome", "Edgar", "Connie", "Nicole", "Russell",
    "Melody", "Edward", "Benjamin", "Madison", "Alison", "Kristie", "Maria", "Beth", "Julie", "Patrick",
    "Alan", "Rhonda", "Katherine", "Kyle", "Valerie", "Bernard", "Tara", "Tasha", "Dakota", "Randy",
    "Warren", "Hailey", "Mario", "Brianna", "Ann", "Vincent", "Sean", "Dawn", "Latoya", "Darlene",
    "Ralph", "Zachary", "Sue", "Jeremiah", "Roberta", "Earl", "Javier", "Melanie", "Harry", "Kelsey",
    "Kurt", "Lorraine", "Brent", "Colin", "Katelyn", "Lindsey", "Bethany", "Cody", "Sandy", "Jose",
    "Rita", "Marco", "Allen", "Cory", "Micheal", "Mathew", "Janice", "Monica", "Sharon", "Elijah",
    "Mason", "Penny", "Dalton", "Phillip", "Joy", "Nichole", "Louis", "Kylie", "Bruce", "Bill",
    "Andres", "Ricky", "Preston", "Johnny", "Leslie", "Marc", "Raven", "Leah", "Marilyn", "Glenn",
    "Molly", "Maureen", "Lonnie", "Shelby", "Dale", "Jane", "Ian", "Howard", "Brett", "Alice",
    "Stanley", "Isaac", "Becky", "Nathaniel", "Vicki", "Jeffery", "Jimmy", "Gwendolyn", "Jodi", "Alexis",
    "Wesley", "Marcus", "Eddie", "Joanne", "Brendan", "Francis", "Terri", "Barbara", "Tracey", "Blake",
    "Morgan", "Grant", "Willie", "Hunter", "Tracie", "Julian", "Cassidy", "Ernest", "Jerry", "Erika",
    "Francisco", "Kayla", "Glen", "Breanna", "Jim", "Marie", "Shane", "Alexander", "Vanessa", "Colleen",
    "Audrey", "Jared", "Caleb", "Carl", "Shaun", "Cassie", "Omar", "Caroline", "Jermaine", "Jorge",
    "Norman", "Kelli", "Kristine", "Makayla", "Jenna", "Debra", "Ricardo", "Monique", "Carolyn", "Kristi",
    "Belinda", "Kendra", "Diamond", "Debbie", "Neil", "Isabella", "Reginald", "Destiny", "Kiara", "Stacie",
    "Tonya", "Billy", "Chris", "Jay", "Yvonne", "Sophia", "Eileen", "Brittney", "Tim", "Frederick",
    "Annette", "Olivia", "Alfred", "Gabriella", "Tommy", "Kaitlyn", "Loretta", "Lawrence", "Mackenzie", "Cesar",
    "Patty", "Sheila", "Antonio", "Cathy", "Gilbert", "Ethan", "Vickie", "Mallory", "Jesus", "Randall",
    "Candace", "Jillian", "Danny", "Connor", "Mckenzie", "Rebekah", "Jeanette", "Devin", "Lynn", "Phyllis",
    "Karina", "Drew", "Kirsten", "Garrett", "Cindy", "Faith", "Joan", "Stefanie", "Alejandro", "Caitlin",
    "Clinton", "Chase", "Jeanne", "Krista", "Meagan", "Jake", "Kari", "Sabrina", "Max", "Logan", "Shirley", "Christy","Traci", "Sierra", "Terrance", "Abigail",
    "Brady", "Alexa", "Adrienne", "Wayne", "Gail", "Zoe", "Philip", "Ray", "Brad", "Roberto",
    "Shelley", "Karl", "Sergio", "Jean", "Stuart", "Shelia", "Carly", "Andre", "Sheri", "Helen",
    "Spencer", "Manuel", "Ellen", "Norma", "Haley", "Collin", "Autumn", "Hector", "Herbert", "Gloria",
    "Cristina", "Miguel", "Darius", "Ronnie", "Jody", "Rose", "Gregg", "Fred", "Tricia", "Roy",
    "Isaiah", "Michaela", "Noah", "Dillon", "Albert", "Mercedes", "Briana", "Leonard", "Kristopher", "Pam",
    "Jocelyn", "Brandy", "Bianca", "Nicolas", "Shawna", "Ruth", "Tammie", "Alvin", "Gabriela", "Selena",
    "Dwayne", "Hayden", "Desiree", "Christie"
]

last_names = [
    "Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez",
    "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson", "Thomas", "Taylor", "Moore", "Jackson", "Martin",
    "Lee", "Perez", "Thompson", "White", "Harris", "Sanchez", "Clark", "Ramirez", "Lewis", "Robinson",
    "Walker", "Young", "Allen", "King", "Wright", "Scott", "Torres", "Nguyen", "Hill", "Flores",
    "Green", "Adams", "Nelson", "Baker", "Hall", "Rivera", "Campbell", "Mitchell", "Carter", "Roberts",
    "Gomez", "Phillips", "Evans", "Turner", "Diaz", "Parker", "Cruz", "Edwards", "Collins", "Reyes",
    "Stewart", "Morris", "Morales", "Murphy", "Cook", "Rogers", "Gutierrez", "Ortiz", "Morgan", "Cooper",
    "Peterson", "Bailey", "Reed", "Kelly", "Howard", "Ramos", "Kim", "Cox", "Ward", "Richardson",
    "Watson", "Brooks", "Chavez", "Wood", "James", "Bennett", "Gray", "Mendoza", "Ruiz", "Hughes",
    "Price", "Alvarez", "Castillo", "Sanders", "Patel", "Myers", "Long", "Ross", "Foster", "Jimenez",
    "Powell", "Jenkins", "Perry", "Russell", "Sullivan", "Bell", "Coleman", "Butler", "Henderson", "Barnes",
    "Gonzales", "Fisher", "Vasquez", "Simmons", "Romero", "Jordan", "Patterson", "Alexander", "Hamilton", "Graham",
    "Reynolds", "Griffin", "Wallace", "Moreno", "West", "Cole", "Hayes", "Bryant", "Herrera", "Gibson",
    "Ellis", "Tran", "Medina", "Aguilar", "Stevens", "Murray", "Ford", "Castro", "Marshall", "Owens",
    "Harrison", "Fernandez", "McDonald", "Woods", "Washington", "Kennedy", "Wells", "Vargas", "Henry", "Chen",
    "Freeman", "Webb", "Tucker", "Guzman", "Burns", "Crawford", "Olson", "Simpson", "Porter", "Hunter",
    "Gordon", "Mendez", "Silva", "Shaw", "Snyder", "Mason", "Dixon", "Munoz", "Hunt", "Hicks",
    "Holmes", "Palmer", "Wagner", "Black", "Robertson", "Boyd", "Rose", "Stone", "Salazar", "Fox",
    "Warren", "Mills", "Meyer", "Rice", "Schmidt", "Garza", "Daniels", "Ferguson", "Nichols", "Stephens",
    "Soto", "Weaver", "Ryan", "Gardner", "Payne", "Grant", "Dunn", "Kelley", "Spencer", "Hawkins"
]

assets_direct = Path(__file__).parent.parent / 'assets'

fnFile = 'firstnamesList.txt'
lnFile = 'lastnamesList.txt'
wordFile = 'wordList.txt'

files = [fnFile,lnFile,wordFile]
wordlists  = [first_names,last_names,words]
files = [assets_direct / f for f in files]

if not assets_direct.exists():
    assets_direct.mkdir()
    for wlist, path in zip(wordlists,files):
        if not path.exists():
            with open(path,'w') as f:
                for idx, word in enumerate(wlist):
                    if idx < len(wlist) -1:
                        f.write(word+'\n')
                    else:
                        f.write(word)