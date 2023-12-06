import { Link, useNavigate } from "react-router-dom";
import image from "../assets/woman.jpg";

function AppointmentSection({ user }) {
  const navigate = useNavigate();
  function handleBook() {
    if (!user) {
      navigate("/login");
    } else {
      navigate("/book_appointment");
    }
  }
  return (
    <div className="home_appointment">
      <div className="appointment_left">
        <img className="appointment_img" src={image} alt="Appointment" />
      </div>
      <div className="appointment_right">
        <h1 className="heading">Lets Go</h1>
        <h1 className="sub-heading">BOOK A VISIT</h1>
        <p>
          Book an appointment today and let us transform your spar visit to an
          experience. You’ll leave feeling pretty on the outside and, more
          importantly, beautiful on the inside. Go from a 9 to a 10!
        </p>
        <button onClick={handleBook} className="booknow">
          Visit now &rarr;
        </button>
      </div>
    </div>
  );
}

export default AppointmentSection;
