import threading
import pygame
import random
import atexit
import sys

def event_handler(event):
    input("Press Enter to continue...")
    event.set()

def display_shapes(event):
    event.wait()
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Geometric Shapes")

    for _ in range(100):
        x = random.randint(50, 750)
        y = random.randint(50, 550)
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        shape_type = random.choice(['circle', 'rectangle'])

        if shape_type == 'circle':
            pygame.draw.circle(screen, color, (x, y), 20)
        else:
            pygame.draw.rect(screen, color, (x, y, 40, 30))

        pygame.display.flip()
        pygame.time.wait(100)

    pygame.quit()

if __name__ == "__main__":
    pygame.init()

    event = threading.Event()

    event_thread = threading.Thread(target=event_handler, args=(event,))
    shapes_thread = threading.Thread(target=display_shapes, args=(event,))

    event_thread.start()
    shapes_thread.start()

    atexit.register(pygame.quit)

    try:
        shapes_thread.join()
    except KeyboardInterrupt:
        print("Simulation terminated.")
        sys.exit(0)
