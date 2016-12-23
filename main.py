from argparse import RawTextHelpFormatter
from queries import *
import argparse
import sys
import os
import re

args = {}
ok_flag = False

def parse_cmd_args():
    global args
    parser = argparse.ArgumentParser(description="""
All indicated required arguments to be provided via -<argname> -value
eg: python main.py -q 1 -75 -y 39 -t 04:04:04
Q1: Is the closest bike station open? [-x, -y, -t]
Q2: Till what time is the closet bike station open? [-x and -y]
Q3: Where can I get a bike at this time? [-t]
Q4: How many bikes are available at a station? [-s]
Q5: Are there any virtual stations nearby for me to book a ride? [-x, -y]
Q6: Which is the closest station that has a trike? [-x, -y]
Q7: Are there any docks for me to use at a station [-s]
Q8: Which stations have trikes?
Q9: Is a station a public station? [-s]
Q10: Where can I leave a bike? [-x, -y, -t]
Q11: Can I leave my bike at the closest station? [-x, -y, -t] 
Q12: What time does a station open? [-s]
Q13: What are the event based stations?
Q14: When and where in the bike stations are the events scheduled?
Q15: Neasrest station with more than 5 bikes?
-----
Q16: Natural Language option for Queries [12, 9, 7]
Just say "<query number> <part_of_station_name>"
Eg: "12 Pine => would print when the station at Pine opens
-----
""", formatter_class=RawTextHelpFormatter)    
    parser.add_argument('-q', '--query', type=int, required = True, help='The query to run')
    parser.add_argument('-x', '--latitude', type=int, default=None, help='The latitude of the user', required = False)
    parser.add_argument('-y', '--longitude', type=int, default=None, help='The longitude of the user', required = False)
    parser.add_argument('-s', '--station', type=str, default=None, help='The station', required = False)
    parser.add_argument('-t', '--time', type=str, default=None, help='The time in hh:mm:ss', required = False)
    args_= parser.parse_args()
    return args_
    

def check_args(*options):
    for arg in options:        
        if arg is None:
            print "Please pass in the reqs as per the usage"
            sys.exit()


def main():
    global args
    args = vars(parse_cmd_args())    
    if args["query"] == 1:
        check_args(args.get("latitude"), args.get("longitude"), args.get("time"))
        query1(args.get("latitude"), args.get("longitude"), args.get("time"))
    elif args["query"] == 2:
        check_args(args.get("latitude"), args.get("longitude"))
        query2(args.get("latitude"), args.get("longitude"))
    elif args["query"] == 3:
        check_args(args.get("time"))
        query3(args.get("time"))
    elif args["query"] == 4:
        check_args(args.get("station"))
        query4(args.get("station"))
    elif args["query"] == 5:
        check_args(args.get("latitude"), args.get("longitude"))
        query5(args.get("latitude"), args.get("longitude"))
    elif args["query"] == 6:
        check_args(args.get("latitude"), args.get("longitude"))
        query6(args.get("latitude"), args.get("longitude"))
    elif args["query"] == 7:
        check_args(args.get("station"))
        query7(args.get("station"))
    elif args["query"] == 8:
        query8()
    elif args["query"] == 9:
        check_args(args.get("station"))
        query9(args.get("station"))
    elif args["query"] == 10:
        check_args(args.get("latitude"), args.get("longitude"), args.get("time"))
        query10(args.get("latitude"), args.get("longitude"), args.get("time"))
    elif args["query"] == 11:
        check_args(args.get("latitude"), args.get("longitude"), args.get("time"))
        query11(args.get("latitude"), args.get("longitude"), args.get("time"))
    elif args["query"] == 12:
        check_args(args.get("station"))
        query12(args.get("station"))
    elif args["query"] == 13:
        query13()
    elif args["query"] == 14:
        query14()
    elif args["query"] == 15:
        check_args(args.get("latitude"), args.get("longitude"), 5)   
        query15(args.get("latitude"), args.get("longitude"), 5)
    elif args["query"] == 16:
        print "State your station specific query in the form \"<tasknum> <whole or part of station name>\", you have a 5 second window"
        stt = os.popen("./rec-speech.sh -d 5")
        quer = stt.read()
        exp = r'(?P<tasknum>\d+) (?P<station>\S+)'
        matches = re.search(exp, quer)
        print matches.group("tasknum")
        print matches.group("station")
        tasknum = int(matches.group("tasknum"))
        station = matches.group("station")
        if tasknum in [12, 9, 7]:
            if tasknum == 12:
                query12(station)
            elif tasknum == 7:
                query7(station)
            elif tasknum == 9:
                query9(station)
        else :
            print "Free form is not applicable to that query index"
    

if __name__ == "__main__":
    """
    Main Sentinel
    """
    main()    