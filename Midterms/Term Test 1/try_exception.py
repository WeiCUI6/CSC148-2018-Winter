# Experiment with exceptions changing what is commented out
# in the try block
class SpecialException(Exception):
    """class docstring here --- child of Exception"""
    pass
class ExtremeException(SpecialException):
    """ grandchild of Exception"""
    pass

if __name__ == '__main__':
    num =1
    denum=0
    try:
        if(denum==0):
        # raise SpecialException('I am a SpecialException')
            raise Exception('I am an Exception')
        # raise ExtremeException('I am an ExtremeException')
        else:
            print(num/denum)
    # block to run if SpecialException was raised
    # use the name se if one is detected
    except ExtremeException as se:
        print(se)
        print('caught as ExtremeException')
    except SpecialException as ee:
        print(ee)
        print('caught as SpecialException')
    except Exception as e:
        print(e)
        print('caught as Exception')

    print('I am outside try')
    print('my code did not stop due to exception')
