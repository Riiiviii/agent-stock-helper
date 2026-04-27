import { Link } from "@tanstack/react-router";
import { Button } from "../ui/button";
import NavbarLink from "./navbar-link";

export default function Navbar() {
  return (
    <nav className="flex justify-between items-center bg-transparent mt-5 mb-5 w-full px-16">
      <div>
        <Button variant="logo" render={<Link to="/" />}>
          V E S T L Y
        </Button>
      </div>
      <div className="flex items-center">
        <NavbarLink href="/" label="Home" variant="navbar" />
        <NavbarLink href="/" label="About" variant="navbar" />
        <NavbarLink href="/" label="Pricing" variant="navbar" />
        <NavbarLink href="/" label="Contact" variant="navbar" />
        <div className="w-px h-4 bg-border mx-2" />
        <NavbarLink href="/" label="Log in" variant="navbar" />
        <NavbarLink href="/" label="Sign up" variant="signup" />
      </div>
    </nav>
  );
}
