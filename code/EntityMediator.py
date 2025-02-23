from code.Const import WIN_WIDTH
from code.Enemy import Enemy
from code.EnemyShoot import EnemyShoot
from code.Entity import Entity
from code.PlayerShoot import PlayerShoot


class EntityMediator:

    @staticmethod
    def __verify_collision_window(ent: Entity):
        if isinstance(ent, Enemy):
            if ent.rect.right <= 0:
                ent.health = 0
        if isinstance(ent, PlayerShoot):
            if ent.rect.left >= WIN_WIDTH:
                ent.health = 0
        if isinstance(ent, EnemyShoot):
            if ent.rect.right <= 0:
                ent.health = 0


    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        for i in range(len(entity_list)):
            teste_entity = entity_list[i]
            EntityMediator.__verify_collision_window(teste_entity)

    @staticmethod
    def verify_health(entity_list: list[Entity]):
        for ent in entity_list:
            if ent.health <= 0:
                entity_list.remove(ent)
