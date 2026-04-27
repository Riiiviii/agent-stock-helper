import { Link } from "@tanstack/react-router";
import { Button } from "../ui/button";

interface NavbarLinkProp {
  href: string;
  label: string;
  exact?: boolean;
}

export default function NavbarLink({ href, label, exact }: NavbarLinkProp) {
  return (
    <Button
      render={<Link to={href} activeOptions={{ exact: exact ?? false }} />}
    >
      {label}
    </Button>
  );
}
