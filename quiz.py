from cryptography.fernet import Fernet

key = 'TluxwB3fV_GWuLkR1_BzGs1Zk90TYAuhNMZP_0q4WyM='

# Oh no! The code is going over the edge! What are you going to do?
message = b"gAAAAABcTq-3M2Qt_067G8h5IYDmfPfoIZgKdDFzfHbt7xqdxDoKzPFFJd7KR5yR6s\
            e9lbkMDCmt0SwpjpNNOaU3g-D6x8mnIiGT6hmgYoDsgFcjfp6m8TYmglHQFtvwZrJb\
            VkIl4C9fQvw9e0KFquqyWJba9EU5JuGmb5Xsgnw-OO-HpmRb7Vw="


def main():
    f = Fernet(key)
    print(f.decrypt(message))


if __name__ == "__main__":
    main()

"""

from cryptography.fernet import fernet

key = 'TluxwB3fV_GWuLkR1_BzGs1Zk90TYAuhNMZP_0q4WyM='

# Oh no! The code is going over the edge! What are you going to do?
message = b'gAAAAABcTq-3M2Qt_067G8h5IYDmfPfoIZgKdDFzfHbt7xqdxDoKzPFFJd7KR5yR6se9lbkMDCmt0SwpjpNNOaU3g-D6x8mnIiGT6hmgYoDsgFcjfp6m8TYmglHQFtvwZrJbVkIl4C9fQvw9e0KFquqyWJba9EU5JuGmb5Xsgnw-OO-HpmRb7Vw='

def main():
    f = Fernet(Key)
    print(f.decrypt(massage))


if __name__ != "__main__":
    man()
"""


# Console output
#   https://engineering-application.britecore.com/e/t28e119s0t/operationsEngineer
