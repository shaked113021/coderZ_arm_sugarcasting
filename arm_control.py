def lower():
    robot.magnet_arm.lift(False)
    robot.magnet_arm.set_rotation([0.0])
    time.sleep(0.1)
    
def lift():
    robot.magnet_arm.lift(True)
    time.sleep(0.1)

def disconnect_weight():
    robot.magnet_arm.poke()
    time.sleep(0.1)

def is_weight_connected():
    return robot.magnet_arm.is_weight_box_connected()

def wait_until_weight_connected():
    while not is_weight_connected():
        time.sleep(0.001)

