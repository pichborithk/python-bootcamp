import os
from flask import Flask, jsonify, render_template, request
import random
from dotenv import load_dotenv

load_dotenv()

from db import db, Cafe

app = Flask(__name__)

# Connect to Database
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DB_PATH")

db.init_app(app)

with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record
@app.route("/random")
def get_random_cafe():
    # random_cafe = db.session.execute(db.select(Cafe).order_by(db.sql.func.random()).limit(1)).scalar()
    result = db.session.execute(db.select(Cafe))
    all_cafes = result.scalars().all()
    random_cafe = random.choice(all_cafes)
    # return jsonify(cafe={
    #     "id": random_cafe.id,
    #     "name": random_cafe.name,
    #     "map_url": random_cafe.map_url,
    #     "img_url": random_cafe.img_url,
    #     "location": random_cafe.location,
    #     "amenities": {
    #         "seats": random_cafe.seats,
    #         "has_toilet": random_cafe.has_toilet,
    #         "has_wifi": random_cafe.has_wifi,
    #         "has_sockets": random_cafe.has_sockets,
    #         "can_take_calls": random_cafe.can_take_calls,
    #         "coffee_price": random_cafe.coffee_price,
    #     }
    # })
    return jsonify(cafe=random_cafe.to_dict())


@app.route("/all")
def get_all_cafe():
    result = db.session.execute(db.select(Cafe))
    all_cafes = result.scalars().all()
    return jsonify(cafes=[cafe.to_dict() for cafe in all_cafes])


@app.route("/search")
def search_cafe():
    # loc = request.args.get("loc")
    # condition = Cafe.location.like(f"%{loc}%")
    # found_cafes = db.session.query(Cafe).where(condition).order_by(Cafe.name)
    # cafes = [cafe.to_dict() for cafe in found_cafes]
    # return jsonify(cafes=cafes) if cafes else jsonify(error=error_not_found(loc)), 404

    query_location = request.args.get("loc")
    result = db.session.execute(db.select(Cafe).where(Cafe.location == query_location))
    all_cafes = result.scalars().all()
    if len(all_cafes) == 0:
        return (
            jsonify(
                error={"Not Found": "Sorry, we don't have a cafe at that location."}
            ),
            404,
        )

    return jsonify(cafes=[cafe.to_dict() for cafe in all_cafes])


# HTTP POST - Create Record
@app.route("/add", methods=["POST"])
def post_new_cafe():
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("loc"),
        has_sockets=bool(request.form.get("sockets")),
        has_toilet=bool(request.form.get("toilet")),
        has_wifi=bool(request.form.get("wifi")),
        can_take_calls=bool(request.form.get("calls")),
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price"),
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})


# HTTP PUT/PATCH - Update Record
@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def update_coffee_price(cafe_id):
    new_price = request.args.get("new_price")
    # select_cafe = db.get_or_404(
    #     Cafe, cafe_id, description=f"Cafe with id: {cafe_id} does not exist."
    # )
    try:
        select_cafe = db.get_or_404(Cafe, cafe_id)
    except Exception as e:
        return jsonify(error=f"{e}"), 404
    else:
        select_cafe.coffee_price = new_price
        db.session.commit()
        return jsonify(response={"success": "Successfully updated the price."})


# HTTP DELETE - Delete Record
@app.route("/report-closed/<int:cafe_id>", methods=["DELETE"])
def delete_cafe(cafe_id):
    api_key = request.args.get("api-key")
    if api_key == "TopSecretAPIKey":
        cafe = db.get_or_404(
            Cafe, cafe_id, description=f"Cafe with id: {cafe_id} does not exist."
        )
        db.session.delete(cafe)
        db.session.commit()
        return (
            jsonify(
                response={"success": "Successfully deleted the cafe from the database."}
            ),
            200,
        )
    return (
        jsonify(
            error={
                "Forbidden": "Sorry, that's not allowed. Make sure you have the correct api_key."
            }
        ),
        403,
    )


# Error Handler
@app.errorhandler(404)
def invalid_route(e):
    return jsonify(error={e.name: e.description}), 404


if __name__ == "__main__":
    app.run(debug=True)
