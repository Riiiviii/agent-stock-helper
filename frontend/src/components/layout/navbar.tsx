import NavbarLink from "./navbar-link";

export default function Navbar() {
  return (
    <nav className="flex justify-between items-center bg-transparent">
      <div>
        <h1>VESTLY</h1>
      </div>
      <div className="flex items-center">
        <NavbarLink href="/" label="Home" />
        <NavbarLink href="/" label="About" />
        <NavbarLink href="/" label="Pricing" />
        <NavbarLink href="/" label="Contact" />
        <div className="w-px h-4 bg-border mx-2" />
        <NavbarLink href="/" label="Log in" />
        <NavbarLink href="/" label="Sign up" />
      </div>
    </nav>
  );
}
