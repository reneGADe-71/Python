import time


class TrafficLight:
    __color = ["RED", "YELLOW", "GREEN"]

    @staticmethod
    def running():
        n = 1
        # Количество повторов включения светофора
        while n <= 2:
            i = 0
            while i < 3:
                print(f"Turn on {TrafficLight.__color[i]}")
                if i == 0:
                    time.sleep(7)
                elif i == 1:
                    time.sleep(2)
                elif i == 2:
                    time.sleep(5)
                i = i + 1
            n = n + 1


TL = TrafficLight()
TL.running()
