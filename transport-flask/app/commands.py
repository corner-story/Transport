from app import app
from app.models import Driver, Consigner, Good, Application
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

    consigners = Consigner.query.all()

    for _ in range(int(goods)):
        good = Good(
            good_name = f.name()
            ,good_type = ["大件","中件","小件"][randint(0,2)]
            ,transport_origin = f.address()
            , transport_des= f.address()
            ,transport_money=f.numerify()
            , good_status=["等待司机承运","选定司机","正在运输","已到达目的地","运输完成"][randint(0,4)]
            ,backup=f.text()
            ,consigner_id= consigners[randint(0, len(consigners)-1)].id
        )
        db.session.add(good)
    
    
    db.session.commit()
    click.echo("Done...")
    
