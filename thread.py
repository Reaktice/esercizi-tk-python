from threading import Thread
import time
from random import randint

class MioThread(Thread):
  def __init__(self,nome,durata):
    Thread.__init__(self)
    self.nome = nome
    self.durata = durata
  def run(self):
    print("Thread "+ self.nome+" avviato")
    time.sleep(self.durata)
    print("Thread "+ self.nome+" terminato")
    

t1 = MioThread("Test", 5)
t1.run()

thread1 = MioThread("uno",randint(1,15))
thread2 = MioThread("due", randint(1,15))
thread3 = MioThread("tre", randint(1,15))
thread1.start()
thread2.start()
thread3.start()

thread1.join()
thread2.join()
thread3.join()

print("Fine")