const mongoose = require("mongoose");

const JokeSchema = new mongoose.Schema(
  {
    setup: {
      type: String,
      required: [true, "Setup is required!"],
      minlength: [6, "Setup must be at least 6 characters!"],
    },
    punchline: {
      type: String,
      required: [true, "Punchline is required!"],
      minlength: [6, "Punchline must be at least 6 characters!"],
    },
  },
  { timestamps: true }
);

const Joke = mongoose.model("Joke", JokeSchema);
module.exports = Joke;
