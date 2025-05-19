def sortirofka(numbers):
    first_element=sorted([i for i in numbers if i%2==0], reverse=True)
    second_element=sorted([i for i in numbers if i%2!=0])

    return first_element+second_element

result=sortirofka(
    list(map(int,input("chisel:").split()))
)
print(result)