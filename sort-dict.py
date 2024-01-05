users = {'1':{'username':'ali24',
        'email':'ali024@g.com',
        'phone': '09166663020'
        },
        '2':{'username':'kami20',
        'email':'kami2@g.com',
        'phone': '09122225030'
        },
        '0':{'username':'mamal19',
        'email':'mamal1919@g.com',
        'phone': '09131988520'
        },
         '3':{'username':'erfan2332',
        'email':'erfanramazani@g.com',
        'phone': '09377536541'
        }
}
print(sorted(users.items(),key=lambda a : a[1]["username"], reverse=True))
