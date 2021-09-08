import logging

logging.basicConfig(level=logging.INFO)


"""
Одно из применений дескрипторов - управление аттрибутами.
С их помощью можно логгировать доступ к аттрибутам, скрывать их, делать приватыми и т.д.
"""


class LoggedAndMakePrivate:

    def __set_name__(self, owner, name):
        self.public_name = name

        postfix = f'_{owner.postfix}' if hasattr(owner, 'postfix') else ''  # просто пример о доступе к owner
        self.private_name = f'_{name}{postfix}'

        logging.info(f'Public name: {self.public_name}')
        logging.info(f'Private name: {self.private_name}')

    def __get__(self, instance, owner):
        logging.info(f'Getting {self.public_name}')
        return getattr(instance, self.private_name)

    def __set__(self, instance, value):
        logging.info(f'Setting {self.public_name}')
        setattr(instance, self.private_name, value)


class Software:
    version = LoggedAndMakePrivate()

    def new_version(self):
        self.version += 1  # вызовется и __get__, и __set__


if __name__ == '__main__':
    logging.info('Create new soft')
    hello_world = Software()
    hello_world.version = 1

    logging.info('Bump version')
    hello_world.new_version()

    logging.info('What version is this?')
    logging.info(f'version: {hello_world.version}')
