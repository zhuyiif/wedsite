"""
Most, if not all of the user-customizable information for the
wedsite can go in here. This makes it easier to port the
project between weddings. This was created in a rough first
pass, please keep updating as time goes on such that when
we go from one friend's site to another we don't need to
much other than change this configuration file.

For the sake of gender-neutrality we'll call the two people
getting married Gride and Broom.
"""
import datetime
import lorem

#
# Gride and Broom
#
FIRST_INITIAL = "first_initial"
FIRST_NAME = "first_name"
LAST_NAME = "last_name"

# Gride info
GRIDE = {
	FIRST_INITIAL : "I",
	FIRST_NAME : "I",
	LAST_NAME : "Really",
}

# Broom info
BROOM = {
	FIRST_INITIAL : "U",
	FIRST_NAME : "Love",
	LAST_NAME : "You",
}

#
# Additional Wedding People.
#

# List of all Gridesmaids
GRIDESMAIDS = (
	{
	    "title" : "Person of Honor",
		"name" : "Important Person",
		"email" : "some_email@wedsite.io",
		"phone" : "(626)-395-1712",
	},

	{
	    "title" : "Gridesmaid",
		"name" : "Slightly Less Important Person",
		"email" : "some_email@wedsite.io",
		"phone" : "(626)-395-1712",
	},

	{
	    "title" : "Gridesmaid",
		"name" : "Slightly Less Important Person",
		"email" : "some_email@wedsite.io",
		"phone" : "(626)-395-1712",
	},

	{
	    "title" : "Gridesmaid",
		"name" : "Slightly Less Important Person",
		"email" : "some_email@wedsite.io",
		"phone" : "(626)-395-1712",
	},
)

# List of all Broomsmen
BROOMSMEN = (
	{
	    "title" : "Best Person",
		"name" : "Important Person",
		"email" : "some_email@wedsite.io",
		"phone" : "(626)-395-1712"
	},

	{
	    "title" : "Broomsman",
		"name" : "Slightly Less Important Person",
		"email" : "some_email@wedsite.io",
		"phone" : "(626)-395-1712"
	},

	{
	    "title" : "Broomsman",
		"name" : "Slightly Less Important Person",
		"email" : "some_email@wedsite.io",
		"phone" : "(626)-395-1712"
	},

	{
	    "title" : "Broomsman",
		"name" : "Slightly Less Important Person",
		"email" : "some_email@wedsite.io",
		"phone" : "(626)-395-1712"
	},
)

# List of people you want to be points of contact for your wedding.
#	This list should be *3 people long* for now to work with the default
#	formatting in contacts.html, otherwise feel free to change the formatting
#	in contacts.html
POINTS_OF_CONTACT = (
	{
		"name" : "Contact Person 1",
		"description" : "Typically Best Person",
		"email" : "some_email@wedsite.io",
		"phone" : "(626)-395-1712"
	},

	{
		"name" : "Contact Person 2",
		"description" : "Typically Person of Honor",
		"email" : "some_email@wedsite.io",
		"phone" : "(626)-395-1712"
	},

	{
		"name" : "Contact Person 3",
		"description" : "Some other poor soul",
		"email" : "some_email@wedsite.io",
		"phone" : "(626)-395-1712"
	},
)

#
#  Rehearsal Dinner info.
#
REHEARSAL_DINNER = {
	"date" : datetime.datetime(2018, 2, 18, 18, 00, 00), # Year, month, day, hour, minute, second
	"location" : {
		"name" : "Some Restaurant",
		"address" : "1234 Tasty Trail",
		"city" : "Flavortown",
		"state" : "CA",
		"zip" : "00000",
		"maps_link" : "https://www.google.com/maps/place/Lloyd+House/@33.9745866,-118.3231545,11z/data=!4m8!1m2!2m1!1slloyd+house!3m4!1s0x80c2c4a868b87301:0x5857f9f8e8bb154b!8m2!3d34.1371511!4d-118.1228224"
	},
	"additional info" : "None",
}

#
# Wedding Ceremony Info
#
WEDDING_CEREMONY = {
	"date" : datetime.datetime(2018, 2, 18, 18, 00, 00), # Year, month, day, hour, minute, second
	"location" : {
		"name" : "Some Religious or Non-Religious Venue",
		"address" : "1234 Love Lane",
		"city" : "Romantic",
		"state" : "CA",
		"zip" : "00000",
		"maps_link" : "https://www.google.com/maps/place/Lloyd+House/@33.9745866,-118.3231545,11z/data=!4m8!1m2!2m1!1slloyd+house!3m4!1s0x80c2c4a868b87301:0x5857f9f8e8bb154b!8m2!3d34.1371511!4d-118.1228224"
	},
	"additional info" : "None",
}

#
# Reception Info
#
WEDDING_RECEPTION = {
	"date" : datetime.datetime(2018, 2, 18, 18, 00, 00), # Year, month, day, hour, minute, second
	"location" : {
		"name" : "Perhaps the same venue, perhaps not",
		"address" : "1234 Party Place",
		"city" : "Funtime",
		"state" : "CA",
		"zip" : "00000",
		"maps_link" : "https://www.google.com/maps/place/Lloyd+House/@33.9745866,-118.3231545,11z/data=!4m8!1m2!2m1!1slloyd+house!3m4!1s0x80c2c4a868b87301:0x5857f9f8e8bb154b!8m2!3d34.1371511!4d-118.1228224"
	},
	"additional info" : "None",
}

#
# Explore Info. This section should be a bit lengthier since you're
#	giving guests ideas about how to spend their time for parts of the
#	weekend you haven't directly scheduled.
#
EXPLORE_AREA_1 = {
	"name" : "The South Bay",
	"map_address" : "South Bay, Los Angeles County, CA",
	"description" : lorem.paragraph(),
}

EXPLORE_AREA_2 = {
	"name" : "Downtown",
	"map_address" : "111 S Grand Ave, Los Angeles, CA 90012",
	"description" : lorem.paragraph(),
}

EXPLORE_AREA_3 = {
	"name" : "Westside",
	"map_address" : "Westside, Los Angeles, CA",
	"description" : lorem.paragraph(),
}

#
# Object that's fed into the templates
#

WEDSITE_JSON = {
	"gride" : GRIDE,
	"broom" : BROOM,
	"gridesmaids" : GRIDESMAIDS,
	"broomemen" : BROOMSMEN,
	"contact" : POINTS_OF_CONTACT,
	"rehearsal" : REHEARSAL_DINNER,
	"ceremony" : WEDDING_CEREMONY,
	"reception" : WEDDING_RECEPTION,
	"explore" : (
		EXPLORE_AREA_1,
		EXPLORE_AREA_2,
		EXPLORE_AREA_3
	),
}