import unittest
import selfdrivingcar


class SelfDrivingCarTest(unittest.TestCase):

    def setUp(self):
        self.car = selfdrivingcar.SelfDrivingCar()

    def test_stop(self):
        self.car.speed = 5
        self.car.stop()
        # Make verifications if speed is equal to 0 after using stop method
        self.assertEqual(self.car.speed, 0)
        # Verify if it is Ok to stop car that is already stopped
        self.car.stop()
        self.assertEqual(self.car.speed, 0)


if __name__ == "__main__":
    unittest.main()
