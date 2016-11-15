import random


def runtime_flashcards():
    """Returns a random runtime question and answer from a dictionary
    https://rob-bell.net/2009/06/a-beginners-guide-to-big-o-notation/

    """

    runtime_dict = {"What is runtime or runtime complexity?": "How quickly the time it takes to run a program grows relative to the input, as the input gets arbitrarily large.",
                    "What is O(1) called?": "Constant time",
                    "What is O(log n) called?": "Logarithmic time",
                    "What is O(n) called?": "Linear runtime",
                    "What is O(n log n) called?": "Loglinear time (a more complex logarithmic runtime)",
                    "What is O(n^2) called?": "Quadratic time",
                    "What is O(2^N) called?": "Exponential time",
                    "What is O(n!) called?": "Factorial time",
                    "Define quadratic": "Involving the second and no higher power of an unknown quantity or variable.",
                    "What is asymptotic behavior?": "The shape that a graph takes as it's line approaches infinity. Big O Notation is a type of asymptotic analysis",
                    "What are the runtimes in order of best to worst?": ["Constant time - O(1)", "Logarithmic time - O(log n)", "Linear time - O(n)", "Loglinear runtime - O(n log n)", "Quadratic time - O(n^2)", "Exponential - O(2^n)", "Factorial time - O(n!)"],
                    "What are the runtimes in order of worst to best?": ["Factorial time - O(n!)", "Exponential - O(2^n)", "Quadratic time - O(n^2)", "Loglinear runtime - O(n log n)", "Linear time - O(n)", "Logarithmic time - O(log n)", "Constant time - O(1)"],
                    "Tell me about O(n)": "Linear runtime means that if your list is n long, it takes n time to do your calculations.",
                    "Tell me about O(1)": "Constant time means that the program will take the same time no matter how large the input.",
                    "Tell me about O(n!)": "Factorial time involves doing something for all possible permutations of the n elements. It is impractical for any reasonably large input size n.",
                    "Tell me about O(2^n)": "Exponential time denotes an algorithm whose growth doubles with each additon to the input data set. The operation is impractical for any reasonably large input size n.",
                    "Tell me about O(log n)": "Logarithmic time means that at every step the work left to check is halved. Logarithmic behavior is typically in a program that divides the input size every step. This could be something like binary search, or an update condition in a for loop",
                    "Tell me about O(n log n)": "Loglinear runtime means that you're performing an O(log n) operation for each item in your input. Most (efficient) sort algorithms are an example of this. Examples are Quicksort and Mergesort. Increasing the input size hurts, but may still be manageable. Every time you double n, you spend twice as much time plus a little more. The operation is only really practical up to a certain input size. Every time n doubles, the operation takes four times as long.",
                    "Tell me about O(n^2)": "Quadratic runtime means that for every element, you do something with every other element, such as comparing them. Such as when you have a recursive function that makes multiple calls, the runtime will often, but not always, look like O(branchesdepth). An example would be password cracking.",
                    "Describe what a graph of constant time would look like?": "Flat",
                    "Which is more desirable, a steep curve or a flat curve?": "Flat",
                    "Give an example of O(1)": "Constant time example: Dictionary lookup or array indexing, Determining if a number is even or odd. Using a constant-size lookup table or hash table.",
                    "Give an example of O(n)": "Linear runtime example: a single for loop or finding an item in an unsorted list.",
                    "Give an example of O(n^2)": "Quadratic time example: two nested for loops, bubble sort, insertion sort",
                    "Give an example of O(n!)": "Factorial time example: Graph traversal. Traveling Salesperson problem",
                    "Give an example of O(log n)": "Logarithmic time example: finding an item in a sorted list with a balanced search tree or a binary search",
                    "Give an example of O(n log n)": "Loglinear runtime example: quicksort (in the average and best case), heapsort and merge sort.",
                    "Give an example of O(2^n)": "Exponential runtime example: if you wanted to break an encryption scheme and you didn't know of any weakness in the encryption scheme. O(2^N) (exponential time) is really bad, which is why strong encryption is so hard to break using a bruteforce approach."
                    }

    return random.sample(runtime_dict.items(), 1)


def flashcard_ajax():
    """Formats html json for an ajax call"""

    card = runtime_flashcards()
    for each in card:
        card = each
    question = card[0]
    answer = card[1]
    font = ""

    if isinstance(answer, list):
        answer = "<br>".join(answer)
    elif len(answer) >= 50:
        font = '<p style="font-size:75%">'

    response_string = '<div class="col-xs-6"><div>{0}</div></div><div class="col-xs-6" id="answer" hidden><div>{1}{2}</div></div>'.format(question, font, answer)

    return response_string
