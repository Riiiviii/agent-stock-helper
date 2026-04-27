import { Link } from "@tanstack/react-router";
import { Button, buttonVariants } from "../ui/button";
import { type VariantProps } from "class-variance-authority";

interface NavbarLinkProp {
  href: string;
  label: string;
  exact?: boolean;
  variant?: VariantProps<typeof buttonVariants>["variant"];
}

export default function NavbarLink({
  href,
  label,
  exact,
  variant = "default",
}: NavbarLinkProp) {
  return (
    <Button
      className="ml-1 mr-1"
      variant={variant}
      render={<Link to={href} activeOptions={{ exact: exact ?? false }} />}
    >
      {label}
    </Button>
  );
}
