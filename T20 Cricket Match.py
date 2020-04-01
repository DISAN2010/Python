"""
S06Q02 : T20 Cricket Match
     - Collect the runs scored for each ball faced by the batsman. 
              A dot ball is represented by a dot in input. 
              An empty line represents a wicket. 

          - Find the total runs scored by the batsman
          - Find the strike rate of the batsman [ runs scored/balls faced ]
          - Find the number of balls wasted by the batsman
          - How many boundaries and sixes did he score ?
"""

def statistics(lst):
    lst = [int(x) for x in lst[:-1]]
    Total_runs = sum(lst)
    Balls = len(lst) + 1 
    Strike_rate = (Total_runs / Balls) * 100
    Balls_wasted = lst.count(0) + 1
    Fours = lst.count(4)
    Sixes = lst.count(6)
    print("Total runs scored by batsmen : ", Total_runs)
    print("Strike rate of the batsmen : ", Strike_rate)
    print("Balls wasted by batsmen : ", Balls_wasted)
    print("Fours scored by batsmen : ", Fours)
    print("Sixes scored by batsmen : ", Sixes)
    
def match(run):
    lst = []
    lst.append(run)
    while 1:
        if run == '':
            print("Out he is gone")
            break
        else:
            run = get_run()
            lst.append(run)

    statistics(lst)

def get_run():
    run = input("Runs scored by batsmen : ")
    if run == '.':
        run = run.replace('.', '0')
    return run

def main():
    Run = get_run()
    while Run == '':
        print("Out for the first ball")
        break
    else:
        match(Run)

#Main starts from here
main()
