from pico2d import *
import random

class Grass:
    # 생성자 함수 초기화 수행
    def __init__(self):
        # Grass 객체의 속성을 정의하고 초기화
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

    def update(self):
        pass

class Boy:
    def __init__(self):
        self.image = load_image('run_animation.png')
        self.x = random.randint(0, 700)
        self.frame = random.randint(0, 7)

    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, 90)

    def update(self):
        self.x += 5
        self.frame = (self.frame + 1) % 8

class Zombie:
    def __init__(self):
        self.x, self.y = 100, 170
        self.frame = 0
        self.image = load_image('zombie_run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 10
        self.x += 5

    def draw(self):
        frame_width = self.image.w // 10
        frame_height = self.image.h
        self.image.clip_draw(self.frame*frame_width, 0, frame_width, frame_height, self.x, self.y, frame_width // 2, frame_height // 2)

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

open_canvas()

def reset_world():
    global running
    global world # World List - 모든 객체를 갖고 있는 리스트

    world = [] # 하나도 객체가 없는 월드
    running = True

    # 땅을 만들고 월드에 추가
    grass = Grass()
    world.append(grass)

    # 소년 11명을 만들고 월드에 추가
    team = [Boy() for _ in range(11)]
    world += team

    zombie = Zombie()
    world.append(zombie)

# 게임 로직
def update_world():
    for game_object in world:
        game_object.update()


def render_world():
    # 월드에 객체들을 그린다.
    clear_canvas()
    for game_object in world:
        game_object.draw()
    update_canvas()

reset_world()

while running:
    handle_events()
    update_world()
    render_world()
    delay(0.05)

close_canvas()
