import random

def draw_lots(arr):
    """
    This function is responsible of the official Christmas present lottery
    Args:
        arr (list): A list of family members to be assigned randomly
    Returns:
        dict: A dictionary where each family member is paired to another family member
    Raises:
        ValueError: If the input list contains fewer than two elements.
    """

    # Condition 1: Should pair each family member to another family member
    # Condition 2: Should not pair a family member to themselves
    # Condition 3: Should return different results on consecutive runs
    # Condition 4: Should throw ValueError if given array contains less than two elements

    # YOUR CODE HERE
    who_whom = {}
    random.shuffle(arr)

    if len(arr) < 3:
        raise ValueError("give more elements plz")
    mones = -1
    for parts in arr:
        who_whom[parts] = arr[mones]
        mones += 1

    return who_whom
    
   
