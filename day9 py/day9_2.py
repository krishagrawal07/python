# #nesting
# capitals = {
#  "france":"Paris",
#  "Germany":"Berlin",
# }

#nesting a list in a dictionary
# travel_log = {
#  "France":["Paris","lille","Dijon"],
#  "Germany":["Berlin","Hamsburg"]
# }

#nesting dictionary in dictionary
travel_log = {
 "France": {"cities visited":["Paris","lille","Dijon"], "total_visits": 12},
 "Germany": {"cities visited": ["Berlin","Hamsburg"], "total_visits": 5},
}

#nesting dictionary in a list
travel_log = [
  {"country": "france", "cities visited":["Paris","lille","Dijon"], "total_visits": 12},
  {"country": "germany", "cities visited": ["Berlin","Hamsburg"], "total_visits": 5},
]


