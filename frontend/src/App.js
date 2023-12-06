// import { Routes, Route, useNavigate } from "react-router-dom";
// import Navbar from "./ui/Navbar";
// import Home from "./pages/Home";
// import Login from "./pages/Login";
// import Signup from "./pages/Signup";
// import Reviews from "./pages/Reviews";
// import HairStudio from "./pages/HairStudio";
// import Makeup from "./pages/Makeup";
// import Contact from "./pages/Contact";
// import Products from "./pages/Products";
// import NailBar from "./pages/NailBar";
// import Appointment from "./pages/Appointment";
// import Footer from "./ui/Footer";
// import { useState, useEffect } from "react";
// import MyAppointments from "./pages/MyAppointments";

// function App  ()  {
//   const navigate = useNavigate();
//   const [user, setUser] = useState(null);

//   useEffect(() => {
//     fetch("/check_session")
//       .then((response) => {
//         if (response.ok) {
//           response.json().then((user) => setUser(user));
//           console.log(user);
//         }
//       })
//       .then((us) => setUser(us));
//   }, []);

//   function handleLogin(user) {
//     setUser(user);
//   }

//   function handleSignup(user) {
//     setUser(user);
//   }

//   function handleLogout() {
//     navigate("/");
//     setUser(null);
//   }

//   const [cartUpdated, setCartUpdated] =useState(false);

//   const addToCart = (productId) => {
//     axios.post('/api/cart/add', { productId }).then(() => {
//       setCartUpdated(!cartUpdated);
//     });
//   }

//   return (
    
//     <>
//       <Navbar user={user} onLogout={handleLogout} />

//       <Routes>
//         <Route path="/" element={<Home user={user} />} />
//         <Route path="/login" element={<Login onLogin={handleLogin} />} />
//         <Route path="/signup" element={<Signup onSignup={handleSignup} />} />
//         <Route path="/reviews" element={<Reviews user={user} />} />
//         <Route path="/products" element={<Products />} />
//         <Route path="/hair_studio" element={<HairStudio />} />
//         <Route path="/make_up" element={<Makeup />} />
//         <Route path="/nail_bar" element={<NailBar />} />
//         <Route path="/contact" element={<Contact />} />
//         <Route path="/book_appointment" element={<Appointment user={user} />} />
//         <Route
//           path="/my_appointments"
//           element={<MyAppointments user={user} />}
//         />
//       </Routes>
//       <Footer />
//     </>
//   //   <div>
//   //   <ProductList addToCart = {addToCart} />
//   //   <Cart key={cartUpdated} />
//   // </div>
//   );
// }

// export default App;

import { Routes, Route, useNavigate } from "react-router-dom";
import Navbar from "./ui/Navbar";
import Home from "./pages/Home";
import Login from "./pages/Login";
import Signup from "./pages/Signup";
import Reviews from "./pages/Reviews";
import HairStudio from "./pages/HairStudio";
import Makeup from "./pages/Makeup";
import Contact from "./pages/Contact";
import Products from "./pages/Products";
import NailBar from "./pages/NailBar";
import Appointment from "./pages/Appointment";
import Footer from "./ui/Footer";
import { useState, useEffect } from "react";
import MyAppointments from "./pages/MyAppointments";
import ProductList from "./ui/ProductList";
import axios from 'axios'; // Add this line

function App() {
  const navigate = useNavigate();
  const [user, setUser] = useState(null);
  const [cartUpdated, setCartUpdated] = useState(false);


  useEffect(() => {
    fetch("/check_session")
      .then((response) => {
        if (response.ok) {
          response.json().then((user) => setUser(user));
          console.log(user);
        }
      })
      .then((us) => setUser(us));
  }, []);

  function handleLogin(user) {
    setUser(user);
  }

  function handleSignup(user) {
    setUser(user);
  }

  function handleLogout() {
    navigate("/");
    setUser(null);
  }
  const addToCart = (product_list_Id) => {
    axios.post('/api/cart/add', { product_list_Id })
      .then(() => setCartUpdated(!cartUpdated))
      .catch((error) => console.error("Error adding to cart:", error));
  }
  // const [cartUpdated, setCartUpdated] = useState(false);

  // const addToCart = (productId) => {
  //   axios.post('/api/cart/add', { productId }).then(() => {
  //     setCartUpdated(!cartUpdated);
  //   });
  // }

  return (
    <>
      <Navbar user={user} onLogout={handleLogout} />

      <Routes>
        <Route path="/" element={<Home user={user} />} />
        <Route path="/login" element={<Login onLogin={handleLogin} />} />
        <Route path="/signup" element={<Signup onSignup={handleSignup} />} />
        <Route path="/reviews" element={<Reviews user={user} />} />
        <Route path="/products" element={<Products addToCart={addToCart} />} />
        <Route path="/product_list" element = {<ProductList addToCart={addToCart} />} />
        <Route path="/hair_studio" element={<HairStudio />} />
        <Route path="/make_up" element={<Makeup />} />
        <Route path="/nail_bar" element={<NailBar />} />
        <Route path="/contact" element={<Contact />} />
        <Route path="/book_appointment" element={<Appointment user={user} />} />
        <Route
          path="/my_appointments"
          element={<MyAppointments user={user} />}
        />
      </Routes>
      <Footer />
    </>
  );
}

export default App;
