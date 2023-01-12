# Quan Yuan
# stable matching


# define Data structure Queue
class Queue:
    def __init__(self, items: list = []):
        self.items = items
    
    def enqueue(self, item: int):
        self.items.append(item)

    def dequeue(self):
        if len(self.items)==0:
            raise RuntimeError("cannot dequeue from empty queue")
        item = self.items[0]
        self.items = self.items[1:]
        return item

    def is_empty(self):
        return len(self.items)==0

    def __str__(self):
        return str(self.items)


# helper function
# return True if student preferes the internship i over the one they currently have
# return False otherwise
# student_ranking(student's queue of internships they prefer)
# contains internships they would prefer over the one they prefer
def student_prefers_i_over_current(student_ranking: Queue, i: int):
    if student_ranking.is_empty():
        return False
    found = False
    helper = Queue([])
    while not student_ranking.is_empty():
        top = student_ranking.dequeue()
        if top != i:
            helper.enqueue(top)
        else:
            found = True
            break
    while not student_ranking.is_empty():
        student_ranking.dequeue()
    while not helper.is_empty():
        student_ranking.enqueue(helper.dequeue())
    return found

# Internships are named 0 to N-1
# students are named N to 2N-1
def find_matches(student_preferences, internship_preferences):
    N = len(student_preferences)
    current_matched = [-1] * N   # student to internship
    available_internships = [True] * N

    # while there are available internships:
        # pick the first available internship
        # until that internship has a match
        # loop through that internship's queue of student preference
            # consider the current top choice student
            # if available
                # update currrent matches
                # update available internships
            # if not available
                # if student prefers this internship
                    # update currrent matches
                    # update available internships for both
    
    while (True) in available_internships:
        for i in range(N):
            if available_internships[i]:
                student = internship_preferences[i].dequeue() - N
                if current_matched[student] == -1:
                    current_matched[student] = i
                    available_internships[i] = False
                else:
                    if student_prefers_i_over_current(student_preferences[student], i):
                        prev_internship = current_matched[student]
                        current_matched[student] = i
                        available_internships[i] = False
                        available_internships[prev_internship] = True

    # return the result: tuple(student, internship)
    result = []
    for i in range(N):
        result.append((i+N, current_matched[i]))
    return result

def main():
    student_preferences = [
        Queue([3,2,1,0]),
        Queue([0,1,2,3]),
        Queue([2,1,0,3]),
        Queue([1,3,2,0])
    ]
    internship_preferences = [
        Queue([7,6,5,4]),
        Queue([5,4,6,7]),
        Queue([4,5,6,7]),
        Queue([6,7,4,5])
    ]
    print(find_matches(student_preferences, internship_preferences))

if __name__=="__main__":
    main()