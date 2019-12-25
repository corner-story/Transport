from app import app
from app.models import Driver, Consigner, Good, Application, GoodType
from app.extensions import db
from faker import Faker
from random import randint
import click



""" 
    生成虚拟数据
"""

@app.cli.command()
def rebuild():
    click.echo("Begin...")
    db.drop_all()
    db.create_all()
    click.echo("Done...")



@app.cli.command()
@click.option("--users", default=20, help="create drivers")
def forge(users):
    click.echo(f"生成{users}条drivers和consigner数据:")
    f = Faker("zh_CN")

    for _ in range(int(users)):
        driver = Driver(
            username = f.name()
            ,password = "123"
            ,phone_number = f.phone_number()
            ,email = f.email()
            ,car_type = ["大货车", "小货车", "中货车"][randint(0,2)]
            ,account = f.credit_card_number()
        )
        
        consigner = Consigner(
            username = f.name()
            ,password = "123"
            ,phone_number = f.phone_number()
            ,email = f.email()
            ,address = f.address()
        )

        db.session.add(driver)
        db.session.add(consigner)
    
    db.session.commit()

    click.echo("Done...")


@app.cli.command()
def forge1(goods=20):
    click.echo(f"生成{goods}条good数据:")
    f = Faker("zh_CN")
    good_types = ["果疏", "金属", "电子器件"]
    good_prices = [1000, 1300, 1400]

    for i in range(len(good_types)):
        goodtype = GoodType(type_name=good_types[i], good_price=good_prices[i])
        db.session.add(goodtype)
    db.session.commit()

    goodtypes = GoodType.query.all()
    consigners = Consigner.query.all()

    for _ in range(int(goods)):
        good = Good(
            good_name = f.name()
            ,goodtype_id = goodtypes[randint(0, len(goodtypes)-1)].id
            ,transport_origin = f.address()
            ,transport_des= f.address()
            ,transport_money=f.numerify()
            ,backup=f.text()
            ,consigner_id= consigners[randint(0, len(consigners)-1)].id
        )
        db.session.add(good)
    
    
    db.session.commit()
    click.echo("Done...")

@app.cli.command()
def forge2(applications=20):
    click.echo(f"生成{applications}条application数据:")
    f = Faker("zh_CN")

    drivers = Driver.query.all()
    goods = Good.query.all()

    for _ in range(int(applications)):
        application = Application(
            backup = f.sentence()
            ,driver_id = drivers[randint(0, len(drivers)-1)].id
            ,good_id= goods[randint(0, len(goods)-1)].id
        )
        db.session.add(application)
    
    db.session.commit()
    click.echo("Done...")
    
