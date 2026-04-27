import { Link } from "@tanstack/react-router";
import NavbarLink from "./navbar-link";
import { Button } from "../ui/button";

export default function Navbar() {
  return (
    <nav className="flex justify-between items-center bg-transparent mt-5 mb-5 w-full px-16">
      <div>
        <Button variant="logo" render={<Link to="/" />}>
          V E S T L Y
        </Button>
      </div>
      <div className="flex items-center">
        <NavbarLink href="/" label="Home" />
        <NavbarLink href="/" label="About" />
        <NavbarLink href="/" label="Pricing" />
        <NavbarLink href="/" label="Contact" />
        <div className="w-px h-4 bg-border mx-2" />
        <NavbarLink href="/" label="Log in" />
        <NavbarLink href="/" label="Sign up" variant="signup" />
      </div>
    </nav>
  );
}
