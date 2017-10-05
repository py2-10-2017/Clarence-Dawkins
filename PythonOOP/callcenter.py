from datetime import datetime

class Call(object):
    num_calls = 0
    def __init__(self,caller,phone_number,reason):
        self.id = Call.num_calls
        self.caller = caller
        self.phone_number = phone_number 
        self. call_time = datetime.now()
        self.reason = reason
        Call.num_calls += 1

    def result(self):
        print ("_" )* 20
        for attr,data in self.__dict__.iteritems():
            if attr == "call_time":
                print "{}:{}".format(attr,data.strftime("%I:%M:%S"))
            else:
                print "{}:{}".format(attr,data)
        print ("_") * 20


class CallCenter(object):
    def __init__(self):
        calls = []
        self.calls = calls
        self.queue_size = self.get_queue_size()

    def get_queue_size(self):
        return len(self.calls)

    def add(self):
        self.calls.append(new_call)
        
        
    def remove(self,rmv_call):
        self.calls.remove(rmv_call) 
        return self

    def info(self):
        for call in self.calls:
            call.result()

def take_call():
    name = raw_input("Thank you for reaching the Call Center.  May I please have your name? ")
    reason = raw_input("May I have the reason for your call today? ")
    phone_number = raw_input("May I have your phone number please? ")
    print "Thank you for the information.  Please hold while I process your call. "
    return Call(name, reason, phone_number)

def call_handle():
    choice = int(input("Would you like to make a call to the Call Center?  Press 1 for YES and 0 for NO "))
    return choice


program = True
center = CallCenter()
while program:
    ring = call_handle()
    if ring == 1:
        center.calls.append(take_call())
        print "Today calls are :"
        center.info()
    else:
        program = False
