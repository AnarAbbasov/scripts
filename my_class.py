class MyClass:
    my_list=[]
    my_dict={}
    my_set=()
    my_tuple=()

    def __init__(self) -> None:
        my_list=[x for x in range(200)]
        my_dic={d for d in range(60)}
        my_set=(s for s in range(400))
        my_tuple=(1,2,3,4,5)


    def show_list():
        print(my_list)
        
