import { Link } from "@tanstack/react-router";
import { Button } from "../ui/button";
import NavbarLink from "./navbar-link";

export default function Navbar() {
  return (
    <nav className="bg-transparent my-5 w-full px-4 sm:px-8 lg:px-16">
      <div className="flex justify-between items-center pb-4">
        <div>
          <Button
            variant="logo"
            aria-label="Vestly home"
            render={<Link to="/" />}
          >
            <span className="tracking-[0.35em]">VESTLY</span>
          </Button>
        </div>
        <div className="hidden md:flex items-center">
          <NavbarLink href="/" label="Home" variant="navbar" />
          <NavbarLink href="/about" label="About" variant="navbar" />
          <NavbarLink href="/pricing" label="Pricing" variant="navbar" />
          <NavbarLink href="/contact" label="Contact" variant="navbar" />
          <div className="w-[0.5px] h-1 bg-gray-400 mx-2" />
          <NavbarLink href="/login" label="Log in" variant="navbar" />
          <NavbarLink href="/signup" label="Sign up" variant="signup" className="px-3 py-1" />
        </div>
      </div>
    </nav>
  );
}
