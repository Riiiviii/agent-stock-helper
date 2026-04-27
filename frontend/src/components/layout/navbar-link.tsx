import { Link, type LinkProps } from "@tanstack/react-router";
import { Button, buttonVariants } from "../ui/button";
import { type VariantProps } from "class-variance-authority";

interface NavbarLinkProp {
  href: LinkProps["to"];
  label: string;
  exact?: boolean;
  variant?: VariantProps<typeof buttonVariants>["variant"];
  className?: string;
}

export default function NavbarLink({
  href,
  label,
  exact = false,
  variant = "default",
  className,
}: NavbarLinkProp) {
  return (
    <Button
      className={`ml-1 mr-1 ${className ?? ""}`}
      variant={variant}
      render={<Link to={href} activeOptions={{ exact }} />}
    >
      {label}
    </Button>
  );
}
