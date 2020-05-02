class CustomSequence:
    '''
    This class when run, creates a infinite loop as getitem and len can help traverse
    a class object but no way to stp it unless we implement __iter__ which helps calling
    StopIteration to stop the loop
    '''

    def __len__(self):
        return 5

    def __getitem__(self, item):
        return f'x{item}'


c = CustomSequence()
# for i in c:
#     print(i)
