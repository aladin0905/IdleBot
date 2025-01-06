from pprint import pprint


x = [
    {
      "memberName": "Tantrid",
      "rank": 2
    },
    {
      "memberName": "Spooniest",
      "rank": 1
    },
    {
      "memberName": "TantridspNUS",
      "rank": 1
    },
    {
      "memberName": "SameEdge",
      "rank": 1
    },
    {
      "memberName": "Messwithme",
      "rank": 1
    },
    {
      "memberName": "RageV1",
      "rank": 1
    },
    {
      "memberName": "RageV2",
      "rank": 0
    },
    {
      "memberName": "Saurry",
      "rank": 0
    },
    {
      "memberName": "TechNus09",
      "rank": 0
    },
    {
      "memberName": "DaveDust",
      "rank": 0
    },
    {
      "memberName": "CityFan",
      "rank": 0
    },
    {
      "memberName": "Brendan",
      "rank": 0
    },
    {
      "memberName": "Forkiest",
      "rank": 0
    },
    {
      "memberName": "TantridWorker1",
      "rank": 0
    },
    {
      "memberName": "TechNus07",
      "rank": 0
    },
    {
      "memberName": "Ker420",
      "rank": 0
    },
    {
      "memberName": "NotSaurry",
      "rank": 0
    },
    {
      "memberName": "Malkero",
      "rank": 0
    },
    {
      "memberName": "Netooz",
      "rank": 0
    },
    {
      "memberName": "DayNight",
      "rank": 0
    }
  ]
y = []
for player in x:
    y.append(player["memberName"])
pprint(y)